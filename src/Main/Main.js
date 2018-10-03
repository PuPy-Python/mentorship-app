import React, { Component } from 'react';
import { Switch, Route, withRouter } from 'react-router-dom';
import Home from './Home/Home';
import Registration from './Register/Registration';

class Main extends Component {
  render() {
    return (
      <div className="Main">
        <Switch>
          <Route exact path="/hello" component={Home} />
          <Route path="/Registration" component={Registration} />
        </Switch>
        <Home />
      </div>
    );
  }
}

export default withRouter(Main);
