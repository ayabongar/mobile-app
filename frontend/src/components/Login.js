import React, { useState } from 'react';
import axios from 'axios';
import Webcam from 'react-webcam';
import './styles.css';

const Login = ({ history }) => {
const [showCamera, setShowCamera] = useState(false);
const [recoverAccount, setRecoverAccount] = useState(false);
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [faceImage, setFaceImage] = useState(null);
  const [message, setMessage] = useState('');

  const handleCapture = (imageSrc) => {
    setFaceImage(imageSrc);
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
        style={{ margin: '10px' }}
        <button type="button" style={{ margin: '10px' }} onClick={() => setShowCamera(true)}>Activate Camera</button>
        {showCamera && (
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
              setShowCamera(false);  // Close the camera once the picture is taken
            }}
          />
        )}
        <button type="button" onClick={() => setShowCamera(true)}>Next</button>
        {showCamera && <Webcam audio={false} screenshotFormat="image/jpeg" height={240} width={320} videoConstraints={{ width: 1280, height: 720, facingMode: 'user', }} onUserMedia={() => { const webcam = document.querySelector('video'); const imageSrc = webcam.getScreenshot(); handleCapture(imageSrc); }} />}
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} />
        <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
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
        <button type="submit">Login</button>
      </form>
      <p>{message}</p>
    </div>
  );
};

export default Login;

