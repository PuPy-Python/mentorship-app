import React from 'react';
import { connect } from 'react-redux';
import { Redirect } from 'react-router';

import LoginForm from '../Login/LoginForm';
import { login } from '../actions/auth';
import { authErrors, isAuthenticated } from '../reducers';

const Login = props => {
  if (props.isAuthenticated) {
    return <Redirect to="/Profile" />;
  }

  return (
    <div className="login-page">
      <LoginForm {...props} />
    </div>
  );
};

const mapStateToProps = state => ({
  errors: authErrors(state),
  isAuthenticated: isAuthenticated(state),
});

const mapDispatchToProps = (dispatch, props) => ({
  onSubmit: (username, password) => {
    dispatch(login(username, password));
    if (props.isAuthenticated) {
      return <Redirect to="/Profile" />;
    }
  },
});

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Login);
