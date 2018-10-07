import React, { Component } from 'react';
import { Switch, Route, withRouter, Redirect } from 'react-router-dom';
import Home from './Home/Home';
import Registration from './Register/Registration';
import Login from './containers/Login';

class Main extends Component {
  render() {
    return (
      <div className="Main">
        <Switch>
          <Route path="/signup" component={Registration} />
          <Route path="/login" component={Login} />
          <Route exact path="/" component={Home} />
          <Redirect to="/" />
        </Switch>
      </div>
    );
  }
}

export default withRouter(Main);
