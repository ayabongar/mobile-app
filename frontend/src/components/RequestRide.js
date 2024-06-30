import React, { useState } from 'react';
import axios from 'axios';

const RequestRide = () => {
  const [username, setUsername] = useState('');
  const [destination, setDestination] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = { username, destination };

    try {
      const response = await axios.post('http://localhost:5000/request_ride', data);
      setMessage(response.data.message);
    } catch (error) {
      setMessage('Request failed!');
    }
  };

  return (
    <div>
      <h2>Request Ride</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} />
        <input type="text" placeholder="Destination" value={destination} onChange={(e) => setDestination(e.target.value)} />
        <button type="submit">Request Ride</button>
      </form>
      <p>{message}</p>
    </div>
  );
};

export default RequestRide;