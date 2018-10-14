import React, { Component } from 'react';
import { Switch, Route, withRouter, Redirect } from 'react-router-dom';
import Registration from './Register/Registration';
import Login from './containers/Login';
import CodeOfConduct from './pages/CodeOfConduct';
import PublicProfileContainer from './Profile/PublicProfileContainer';

class Main extends Component {
  render() {
    document.title = 'PuPPy Mentorship App';
    return (
      <div className="Main">
        <Switch>
          <Route exact path="/" component={Login} />
          <Route path="/signup" component={Registration} />
          <Route path="/code-of-conduct" component={CodeOfConduct} />
          <Route path="/Profile/:username?" component={PublicProfileContainer} />
          <Redirect to="/" />
        </Switch>
      </div>
    );
  }
}

export default withRouter(Main);
