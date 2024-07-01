import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Register from './components/Register';
import Login from './components/Login';
import LandingPage from './components/LandingPage';
import RequestRide from './components/RequestRide';

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route path="/register" component={Register} />
          <Route path="/login" component={Login} />
          <Route path="/request-ride" component={RequestRide} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
