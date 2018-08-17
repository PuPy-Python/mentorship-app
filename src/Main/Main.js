import React, { Component } from 'react';
import { Switch, Route, Redirect, withRouter, BrowserRouter } from 'react-router-dom';

import { Provider, connect } from "react-redux";
import { createStore, applyMiddleware } from "redux";
import thunk from "redux-thunk";

import {auth} from "./actions";
import mentyApp from "./reducer";

import Home from './Home/Home';
import HelloWorld from './HelloWorld';
import Register from './Register/MentorRegister';
import Login from './Login/loginform/login';

let store = createStore(mentyApp, applyMiddleware(thunk));


class RootContainerComponent extends Component {

  componentDidMount() {
    this.props.loadUser();
  }

  PrivateRoute = ({component: ChildComponent, ...rest}) => {
    return <Route {...rest} render={props => {
      if (this.props.auth.isLoading) {
        return <em>Loading...</em>;
      } else if (!this.props.auth.isAuthenticated) {
        return <Redirect to="/login" />;
      } else {
        return <ChildComponent {...props} />
      }
    }} />
  }
  render() {
    let {PrivateRoute} = this;
    return (
    <div className="Main">
    <Switch>
      <Route path ='/hello/register' component={Register}/>
      <Route exact path="/hello" component={Home} />
      <PrivateRoute exact path="/" component={HelloWorld} />
      <Route exact path ='/hello/login' component={Login}/>
      <Redirect to="/hello" />
      </Switch>
      </div>
    );
  }
}
const mapStateToProps = state => {
  return {
    auth: state.auth,
  }
}

const mapDispatchToProps = dispatch => {
  return {
    loadUser: () => {
      return dispatch(auth.loadUser());
    }
  }
}

let RootContainer = connect(mapStateToProps, mapDispatchToProps)(RootContainerComponent);

export default class App extends Component {
  render() {
    return (
    <Provider store={store}>
    <RootContainer />
    </Provider>
    )
  }
}



// class Main extends Component {
//   render() {
//     return (
      
//     );
//   }
// }

// export default withRouter(Main);
