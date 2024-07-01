import React, { useState } from 'react';
import axios from 'axios';
import Webcam from 'react-webcam';
import './styles.css';

const Register = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [role, setRole] = useState('');
  const [faceImage, setFaceImage] = useState(null);
  const [message, setMessage] = useState('');

  const handleCapture = (imageSrc) => {
    setFaceImage(imageSrc);
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
    <div className="form-container">
      <h2>Register</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} />
        <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
        <input type="text" placeholder="Role (user/driver)" value={role} onChange={(e) => setRole(e.target.value)} />
        <Webcam
          audio={false}
          screenshotFormat="image/jpeg"
          height={240}
          width={320}
          videoConstraints={{
            width: 1280,
            height: 720,
            facingMode: 'user',
          }}
          onUserMedia={() => {
            const webcam = document.querySelector('video');
            const imageSrc = webcam.getScreenshot();
            handleCapture(imageSrc);
          }}
        />
        <button type="submit">Register</button>
      </form>
      <p>{message}</p>
    </div>
  );
};

export default Register;

export default Register;
