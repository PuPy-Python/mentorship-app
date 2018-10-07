import React, { Component } from 'react';
import { Switch, Route, withRouter, Redirect } from 'react-router-dom';
import Home from './Home/Home';
import Registration from './Register/Registration';
import Login from './containers/Login';
import CodeOfConduct from './pages/CodeOfConduct'

class Main extends Component {
  render() {
    document.title = "PuPPy Mentorship App";
    return (
      <div className="Main">
        <Switch>
          <Route exact path="/" component={Home} />
          <Route path="/signup" component={Registration} />
          <Route path="/login" component={Login} />
          <Route path="/code-of-conduct" component={CodeOfConduct} />
          <Redirect to="/" />
        </Switch>
      </div>
    );
  }
}

export default withRouter(Main);
