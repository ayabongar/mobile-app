import React, { useState } from 'react';
import axios from 'axios';
import Webcam from 'react-webcam';
import './styles.css';

const Register = () => {
  const [username, setUsername] = useState('');
const [confirmPassword, setConfirmPassword] = useState('');
const [passwordStrength, setPasswordStrength] = useState('');
const [showCamera, setShowCamera] = useState(false);
const [confirmPassword, setConfirmPassword] = useState('');
const [passwordStrength, setPasswordStrength] = useState('');
const [showCamera, setShowCamera] = useState(false);
const validatePasswordStrength = (password) => {
  const regex = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
  return regex.test(password);
};
const [confirmPassword, setConfirmPassword] = useState('');
const [passwordStrength, setPasswordStrength] = useState('');
const [showCamera, setShowCamera] = useState(false);
  const [password, setPassword] = useState('');
  const [role, setRole] = useState('user');
  const [role, setRole] = useState('');
  const [faceImage, setFaceImage] = useState(null);
  const [message, setMessage] = useState('');

  const handleCapture = (imageSrc) => {
    setFaceImage(imageSrc);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    } catch (error) {
      setMessage('Registration failed!');
    }
  };

  return (
    <div className="form-container">
      <h2>Register</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} />
        <input type="password" placeholder="Password" value={password} onChange={(e) => {
          setPassword(e.target.value);
          setPasswordStrength(validatePasswordStrength(e.target.value) ? 'Strong' : 'Weak');
        }} />
        <input type="password" placeholder="Confirm Password" value={confirmPassword} onChange={(e) => setConfirmPassword(e.target.value)} />
        {password !== confirmPassword && <p>Passwords do not match!</p>}
        <p>{passwordStrength}</p>
      setMessage('Registration failed!');
    }
        <button type="button" onClick={() => setShowCamera(true)}>Activate Camera</button>
        {showCamera && <Webcam audio={false} screenshotFormat="image/jpeg" height={240} width={320} videoConstraints={{ width: 1280, height: 720, facingMode: 'user', }} onUserMedia={() => { const webcam = document.querySelector('video'); const imageSrc = webcam.getScreenshot(); handleCapture(imageSrc); }} />}
  };

  return (
        <input type="password" placeholder="Confirm Password" value={confirmPassword} onChange={(e) => setConfirmPassword(e.target.value)} />
        {password !== confirmPassword && <p>Passwords do not match!</p>}
        <p>{passwordStrength}</p>
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
