import React, { useState, useRef } from 'react';
import axios from 'axios';
import Webcam from 'react-webcam';
import './styles.css';

const Login = ({ history }) => {
  const [showCamera, setShowCamera] = useState(false);
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [faceImage, setFaceImage] = useState(null);
  const [message, setMessage] = useState('');
  const webcamRef = useRef(null);

  const handleCapture = () => {
    const imageSrc = webcamRef.current.getScreenshot();
    setFaceImage(imageSrc);
    setShowCamera(false);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('username', username);
    if (password) formData.append('password', password);
    if (faceImage) formData.append('face_image', faceImage);

    try {
      const response = await axios.post('http://localhost:5000/login', formData);
      setMessage(response.data.message);
      if (response.data.message.includes('successful')) {
        history.push('/request-ride');
      }
    } catch (error) {
      setMessage('Login failed!');
    }
  };

  return (
    <div className="form-container">
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} />
        <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
        <button type="button" onClick={() => setShowCamera(true)}>Activate Camera</button>
        {showCamera && (
          <div>
            <Webcam
              audio={false}
              ref={webcamRef}
              screenshotFormat="image/jpeg"
              height={240}
              width={320}
              videoConstraints={{
                width: 1280,
                height: 720,
                facingMode: 'user',
              }}
            />
            <button type="button" onClick={handleCapture}>Capture Image</button>
          </div>
        )}
        <button type="submit">Login</button>
      </form>
      <p>{message}</p>
    </div>
  );
};

export default Login;
