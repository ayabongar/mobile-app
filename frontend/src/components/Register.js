import React, { useState } from 'react';
import axios from 'axios';

const Register = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [role, setRole] = useState('');
  const [faceImage, setFaceImage] = useState(null);
  const [message, setMessage] = useState('');

  const handleFileChange = (e) => {
    setFaceImage(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);
    formData.append('role', role);
    formData.append('face_image', faceImage);

    try {
      const response = await axios.post('http://localhost:5000/register', formData);
      setMessage(response.data.message);
    } catch (error) {
      setMessage('Registration failed!');
    }
  };

  return (
    <div>
      <h2>Register</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} />
        <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
        <input type="text" placeholder="Role (user/driver)" value={role} onChange={(e) => setRole(e.target.value)} />
        <input type="file" onChange={handleFileChange} />
        <button type="submit">Register</button>
      </form>
      <p>{message}</p>
    </div>
  );
};

export default Register;