import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { withStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import styles from '../index.css';

class Header extends Component {
  render() {
    return (
      <AppBar position="static">
        <Toolbar>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/signup">Sign Up</Link>
            </li>
            <li>
              <Link to="/code-of-conduct">Code of Conduct</Link>
            </li>
            <li>
              <Link to="/Profile">Your Profile</Link>
            </li>
          </ul>
        </Toolbar>
      </AppBar>
    );
  }
}

export default withStyles(styles)(Header);
