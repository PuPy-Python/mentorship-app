import React, { Component } from 'react';
import superagent from 'superagent';
import Constants from '../constants';

class HelloWorld extends Component {
  constructor(props) {
    super(props);
    this.state = {
      message: '',
    };
  }

  componentDidMount() {
    superagent.get(`${Constants.API_URL}/helloworld`).end((err, res) => {
      this.setState({
        message: res.body['message'],
      });
    });
  }

  render() {
    return (
      <div className="HelloWorld">
        <p>{this.state.message}</p>
      </div>
    );
  }
}

export default HelloWorld;
