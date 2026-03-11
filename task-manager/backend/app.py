from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from datetime import datetime, timezone

app = Flask(__name__)
CORS(app)

DB_PATH = "tasks.db"


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            title     TEXT    NOT NULL,
            priority  TEXT    NOT NULL CHECK(priority IN ('Low', 'Medium', 'High')),
            completed BOOLEAN NOT NULL DEFAULT 0,
            created_at TEXT   NOT NULL
        )
    """)
    conn.commit()
    conn.close()


init_db()


# ── Helper ──────────────────────────────────────────────────
def row_to_dict(row):
    return {
        "id":         row["id"],
        "title":      row["title"],
        "priority":   row["priority"],
        "completed":  bool(row["completed"]),
        "created_at": row["created_at"],
    }


# ── 1. Create Task ───────────────────────────────────────────
@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    title = (data.get("title") or "").strip()
    priority = data.get("priority", "").strip()

    if not title:
        return jsonify({"error": "Title is required."}), 400
    if priority not in ("Low", "Medium", "High"):
        return jsonify({"error": "Priority must be Low, Medium, or High."}), 400

    created_at = datetime.now(timezone.utc).isoformat()

    conn = get_db()
    cursor = conn.execute(
        "INSERT INTO tasks (title, priority, completed, created_at) VALUES (?, ?, ?, ?)",
        (title, priority, 0, created_at),
    )
    conn.commit()
    task_id = cursor.lastrowid
    task = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
    conn.close()

    return jsonify(row_to_dict(task)), 201


# ── 2 & 3. View All Tasks + Filter ──────────────────────────
@app.route("/tasks", methods=["GET"])
def get_tasks():
    priority  = request.args.get("priority")   # Low | Medium | High
    completed = request.args.get("completed")  # "true" | "false"

    query  = "SELECT * FROM tasks WHERE 1=1"
    params = []

    if priority and priority in ("Low", "Medium", "High"):
        query += " AND priority = ?"
        params.append(priority)

    if completed is not None:
        completed_bool = 1 if completed.lower() == "true" else 0
        query += " AND completed = ?"
        params.append(completed_bool)

    query += " ORDER BY created_at DESC"

    conn  = get_db()
    rows  = conn.execute(query, params).fetchall()
    conn.close()

    return jsonify([row_to_dict(r) for r in rows]), 200


# ── 4. Toggle Completion ─────────────────────────────────────
@app.route("/tasks/<int:task_id>/toggle", methods=["PATCH"])
def toggle_task(task_id):
    conn = get_db()
    task = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()

    if not task:
        conn.close()
        return jsonify({"error": "Task not found."}), 404

    new_status = 0 if task["completed"] else 1
    conn.execute("UPDATE tasks SET completed = ? WHERE id = ?", (new_status, task_id))
    conn.commit()

    updated = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
    conn.close()

    return jsonify(row_to_dict(updated)), 200


# ── 5. Delete Task ────────────────────────────────────────────
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    conn = get_db()
    task = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()

    if not task:
        conn.close()
        return jsonify({"error": "Task not found."}), 404

    conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

    return jsonify({"message": f"Task {task_id} deleted successfully."}), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)
