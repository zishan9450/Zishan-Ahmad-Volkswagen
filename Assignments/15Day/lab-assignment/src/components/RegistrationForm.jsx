import { useState } from "react";

function RegistrationForm({ onRegister }) {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    phone: "",
    address: "",
  });

  const [errors, setErrors] = useState({});

  const validate = () => {
    const newErrors = {};
    if (!formData.name.trim()) newErrors.name = "Name is required";
    if (!formData.email.trim()) newErrors.email = "Email is required";
    else if (!/\S+@\S+\.\S+/.test(formData.email))
      newErrors.email = "Invalid email format";
    if (!formData.phone.trim()) newErrors.phone = "Phone number is required";
    else if (!/^\d{10}$/.test(formData.phone))
      newErrors.phone = "Phone must be 10 digits";
    return newErrors;
  };

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const validationErrors = validate();
    if (Object.keys(validationErrors).length > 0) {
      setErrors(validationErrors);
    } else {
      setErrors({});
      onRegister(formData);
    }
  };

  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <h2 style={styles.title}>Register</h2>
        <form onSubmit={handleSubmit}>

          <div style={styles.field}>
            <label>Name</label>
            <input
              type="text"
              name="name"
              value={formData.name}
              onChange={handleChange}
              style={styles.input}
              placeholder="Enter your name"
            />
            {errors.name && <p style={styles.error}>{errors.name}</p>}
          </div>

          <div style={styles.field}>
            <label>Email</label>
            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              style={styles.input}
              placeholder="Enter your email"
            />
            {errors.email && <p style={styles.error}>{errors.email}</p>}
          </div>

          <div style={styles.field}>
            <label>Phone Number</label>
            <input
              type="text"
              name="phone"
              value={formData.phone}
              onChange={handleChange}
              style={styles.input}
              placeholder="10-digit phone number"
            />
            {errors.phone && <p style={styles.error}>{errors.phone}</p>}
          </div>

          <div style={styles.field}>
            <label>Address (Optional)</label>
            <input
              type="text"
              name="address"
              value={formData.address}
              onChange={handleChange}
              style={styles.input}
              placeholder="Enter your address"
            />
          </div>

          <button type="submit" style={styles.button}>
            Register
          </button>
        </form>
      </div>
    </div>
  );
}

const styles = {
  container: {
    display: "flex", justifyContent: "center",
    alignItems: "center", minHeight: "100vh",
    backgroundColor: "#f0f2f5",
  },
  card: {
    backgroundColor: "#fff", padding: "2rem",
    borderRadius: "10px", boxShadow: "0 4px 12px rgba(0,0,0,0.1)",
    width: "100%", maxWidth: "420px",
  },
  title: { textAlign: "center", marginBottom: "1.5rem", color: "#333" },
  field: { marginBottom: "1rem", display: "flex", flexDirection: "column" },
  input: {
    padding: "0.6rem 0.8rem", borderRadius: "6px",
    border: "1px solid #ccc", marginTop: "0.3rem", fontSize: "0.95rem",
  },
  error: { color: "red", fontSize: "0.8rem", marginTop: "0.2rem" },
  button: {
    width: "100%", padding: "0.75rem", backgroundColor: "#4f46e5",
    color: "#fff", border: "none", borderRadius: "6px",
    fontSize: "1rem", cursor: "pointer", marginTop: "0.5rem",
  },
};

export default RegistrationForm;
