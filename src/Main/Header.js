import React, { Component } from 'react';
import { Link } from 'react-router-dom';

class Header extends Component{
  render(){
    return(
      <header>
        <nav>
          <ul>
            <li><Link to="/hello"> Hello Home</Link></li>
            <li><Link to="/Register/Register"> Register</Link></li>
          </ul>
        </nav>
      </header>
  );
        }
}

<<<<<<< HEAD
export default Header
=======
export default Header
>>>>>>> feature/register
