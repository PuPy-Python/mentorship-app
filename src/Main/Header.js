import Menu from '@material-ui/core/Menu';
import React, { Component } from 'react';
import { Link } from 'react-router-dom';

class Header extends Component {
  render() {
    return (
      <header>
        <nav className="navbar navbar-expand-lg navbar-dark bg-primary">
          <ul>
            <li>
              <Link to="/">PuPPy Mentorship</Link>
            </li>
            <li>
              <Link to="/register">Sign Up</Link>
            </li>
            <li>
              <Link to="/login">Login</Link>
            </li>
            <li>
              <Link to="/code-of-conduct">Code of Conduct</Link>
            </li>
          </ul>
        </nav>
      </header>
    );
  }
}

export default Header;
