import React, { Component } from 'react';
import { Switch, Route, withRouter } from 'react-router-dom';
import Home from './Home/Home';
import Registration from './Register/Registration';
import LoginForm from './Login/LoginForm';

class Main extends Component {
  render() {
    return (
      <div className="Main">
        <Switch>
          <Route exact path="/" component={Home} />
          <Route path="/signup" component={Registration} />
          <Route path="/login" component={LoginForm} />
        </Switch>
      </div>
    );
  }
}

export default withRouter(Main);
