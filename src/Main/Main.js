import React, { Component } from 'react';
import { Switch, Route, Redirect, withRouter, BrowserRouter } from 'react-router-dom';

import { Provider, connect } from "react-redux";
import { createStore, applyMiddleware } from "redux";
import thunk from "redux-thunk";

import {auth} from "./actions";
import state from './reducer'

import Home from './Home/Home';
import HelloWorld from './HelloWorld';
import Register from './Register/MentorRegister';
import Login from './Login/loginform/login'


class Main extends Component {
  render() {
    return (
      <div className="Main">
        <Switch>
          <Route exact path="/hello" component={Home} />
          <Route path="/hello/helloworld" component={HelloWorld} />
          <Route path ='/hello/register' component={Register}/>
          <Route path ='/hello/login' component={Login}/>
          <Redirect to="/hello" />
        </Switch>
      </div>
    );
  }
}

export default withRouter(Main);
