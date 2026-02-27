function Dashboard({ user, onLogout }) {
  return (
    <div style={styles.page}>

      {/* Top Navbar */}
      <nav style={styles.navbar}>
        <span style={styles.brand}>MyApp</span>
        <div style={styles.navRight}>
          <span style={styles.welcome}>Welcome, {user.name} 👋</span>
          <button onClick={onLogout} style={styles.logoutBtn}>
            Logout
          </button>
        </div>
      </nav>

      {/* User Details Card */}
      <div style={styles.container}>
        <div style={styles.card}>
          <h2 style={styles.heading}>Registration Details</h2>
          <table style={styles.table}>
            <tbody>
              <tr>
                <td style={styles.label}>Name</td>
                <td style={styles.value}>{user.name}</td>
              </tr>
              <tr>
                <td style={styles.label}>Email</td>
                <td style={styles.value}>{user.email}</td>
              </tr>
              <tr>
                <td style={styles.label}>Phone</td>
                <td style={styles.value}>{user.phone}</td>
              </tr>
              <tr>
                <td style={styles.label}>Address</td>
                <td style={styles.value}>{user.address || "N/A"}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

    </div>
  );
}

const styles = {
  page: { minHeight: "100vh", backgroundColor: "#f0f2f5" },
  navbar: {
    display: "flex", justifyContent: "space-between",
    alignItems: "center", padding: "1rem 2rem",
    backgroundColor: "#4f46e5", color: "#fff",
    boxShadow: "0 2px 8px rgba(0,0,0,0.2)",
  },
  brand: { fontSize: "1.4rem", fontWeight: "bold" },
  navRight: { display: "flex", alignItems: "center", gap: "1rem" },
  welcome: { fontSize: "1rem" },
  logoutBtn: {
    padding: "0.4rem 1rem", backgroundColor: "#fff",
    color: "#4f46e5", border: "none", borderRadius: "6px",
    cursor: "pointer", fontWeight: "bold",
  },
  container: {
    display: "flex", justifyContent: "center",
    alignItems: "center", padding: "3rem 1rem",
  },
  card: {
    backgroundColor: "#fff", padding: "2rem",
    borderRadius: "10px", boxShadow: "0 4px 12px rgba(0,0,0,0.1)",
    width: "100%", maxWidth: "500px",
  },
  heading: { marginBottom: "1.5rem", color: "#333" },
  table: { width: "100%", borderCollapse: "collapse" },
  label: {
    fontWeight: "bold", padding: "0.6rem 1rem 0.6rem 0",
    color: "#555", width: "40%",
  },
  value: { padding: "0.6rem 0", color: "#222" },
};

export default Dashboard;
