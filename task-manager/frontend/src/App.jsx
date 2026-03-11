import { useEffect, useState } from "react";
import "./App.css";

const PRIORITIES = ["", "Low", "Medium", "High"];

export default function App() {
  const [tasks, setTasks]             = useState([]);
  const [title, setTitle]             = useState("");
  const [priority, setPriority]       = useState("Medium");
  const [error, setError]             = useState("");

  // Filter state
  const [filterPriority,  setFilterPriority]  = useState("");
  const [filterCompleted, setFilterCompleted] = useState("");

  // ── Fetch Tasks ────────────────────────────────────────────
  const fetchTasks = async () => {
    const params = new URLSearchParams();
    if (filterPriority)  params.append("priority",  filterPriority);
    if (filterCompleted) params.append("completed", filterCompleted);

    const res  = await fetch(`/tasks?${params.toString()}`);
    const data = await res.json();
    setTasks(data);
  };

  useEffect(() => {
    fetchTasks();
  }, [filterPriority, filterCompleted]); // re-fetch whenever filter changes

  // ── Create Task ────────────────────────────────────────────
  const handleCreate = async (e) => {
    e.preventDefault();
    setError("");

    if (!title.trim()) { setError("Title is required."); return; }

    const res  = await fetch("/tasks", {
      method:  "POST",
      headers: { "Content-Type": "application/json" },
      body:    JSON.stringify({ title, priority }),
    });
    const data = await res.json();

    if (!res.ok) { setError(data.error); return; }

    setTitle("");
    setPriority("Medium");
    fetchTasks();
  };

  // ── Toggle Completion ──────────────────────────────────────
  const handleToggle = async (id) => {
    await fetch(`/tasks/${id}/toggle`, { method: "PATCH" });
    fetchTasks();
  };

  // ── Delete Task ────────────────────────────────────────────
  const handleDelete = async (id) => {
    await fetch(`/tasks/${id}`, { method: "DELETE" });
    fetchTasks();
  };

  // ── Priority Badge Color ───────────────────────────────────
  const badgeClass = (p) =>
    p === "High" ? "badge high" : p === "Medium" ? "badge medium" : "badge low";

  return (
    <div className="container">
      <h1>📋 Task Manager</h1>

      {/* ── Create Form ───────────────────────────────────── */}
      <form className="task-form" onSubmit={handleCreate}>
        <input
          type="text"
          placeholder="Task title…"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <select value={priority} onChange={(e) => setPriority(e.target.value)}>
          <option value="Low">Low</option>
          <option value="Medium">Medium</option>
          <option value="High">High</option>
        </select>
        <button type="submit">Add Task</button>
      </form>
      {error && <p className="error">{error}</p>}

      {/* ── Filter Controls ───────────────────────────────── */}
      <div className="filters">
        <label>Filter by Priority:</label>
        <select value={filterPriority} onChange={(e) => setFilterPriority(e.target.value)}>
          {PRIORITIES.map((p) => (
            <option key={p} value={p}>{p || "All"}</option>
          ))}
        </select>

        <label style={{ marginLeft: "1rem" }}>
          <input
            type="checkbox"
            checked={filterCompleted === "true"}
            onChange={(e) =>
              setFilterCompleted(e.target.checked ? "true" : "")
            }
          />
          &nbsp;Show Completed Only
        </label>
      </div>

      {/* ── Task Table ────────────────────────────────────── */}
      {tasks.length === 0 ? (
        <p className="empty">No tasks found.</p>
      ) : (
        <table>
          <thead>
            <tr>
              <th>#</th>
              <th>Title</th>
              <th>Priority</th>
              <th>Status</th>
              <th>Created At</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {tasks.map((task, idx) => (
              <tr key={task.id} className={task.completed ? "done" : ""}>
                <td>{idx + 1}</td>
                <td>{task.title}</td>
                <td><span className={badgeClass(task.priority)}>{task.priority}</span></td>
                <td>{task.completed ? "✅ Done" : "⏳ Pending"}</td>
                <td>{new Date(task.created_at).toLocaleString()}</td>
                <td className="actions">
                  <button
                    className="btn-toggle"
                    onClick={() => handleToggle(task.id)}
                  >
                    {task.completed ? "Undo" : "Complete"}
                  </button>
                  <button
                    className="btn-delete"
                    onClick={() => handleDelete(task.id)}
                  >
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}
