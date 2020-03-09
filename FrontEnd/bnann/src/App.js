import React from 'react';
import Home from './Routes/Home.js'
import About from './Routes/About/About.js'

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import './App.css';

export default function App() {
  return (
    <Router>
      <div className='root'>
        <nav className='navBar'>
            <div className='navButton'>
              <Link to="/">Home</Link>
            </div>
            <div className='navButton'>
              <Link to="/about">About</Link>
            </div>
        </nav>

        {/* A <Switch> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
        <Switch>
          <Route path="/about">
            <About />
          </Route>
          <Route path="/">
            <Home />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}
