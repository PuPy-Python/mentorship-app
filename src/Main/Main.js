import React, { Component } from 'react';
import { Switch, Route, Redirect, withRouter } from 'react-router-dom';
import Home from './Home/Home';
import HelloWorld from './HelloWorld';

class Main extends Component {
  render() {
    return (
      <div className="Main">
        <Switch>
          <Route exact path="/hello" component={Home} />
          <Route path="/hello/helloworld" component={HelloWorld} />
          <Redirect to="/hello" />
        </Switch>
      </div>
    );
  }
}

export default withRouter(Main);
