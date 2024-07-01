import React from 'react';
import { Link } from 'react-router-dom';
import './styles.css';

const LandingPage = () => {
  return (
    <div className="landing-container">
      <h2>Welcome to the E-Hailing App</h2>
      <div className="button-container">
        <Link to="/register">
          <button>Register</button>
        </Link>
        <Link to="/login">
          <button>Login</button>
        </Link>
      </div>
    </div>
  );
};

export default LandingPage;
