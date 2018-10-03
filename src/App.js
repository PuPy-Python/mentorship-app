import React, { Component } from 'react';
import { BrowserRouter } from 'react-router-dom';
import Main from './Main/Main';
import Header from './Main/Header';
import { connect } from 'react-redux';
import { echo } from './Main/actions/echo';
import { serverMessage } from './Main/reducers';

export class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <div className="App">
          <Header />
          <Main />
        </div>
      </BrowserRouter>
    );
  }
}

export default connect(
  state => ({ message: serverMessage(state) }),
  { fetchMessage: echo }
)(App);
