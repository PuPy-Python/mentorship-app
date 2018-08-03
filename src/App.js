import React, { Component } from 'react';
import { BrowserRouter } from 'react-router-dom';
import Main from './Main/Main';
import Header from './Main/Header'

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <div className="App">
          <Header/>
          <Main />
        </div>
      </BrowserRouter>
    );
  }
}

export default App;
