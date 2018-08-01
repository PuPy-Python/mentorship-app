import React, { Component } from 'react';
import superagent from 'superagent';
import { HELLO_WORLD_URL } from '../constants';

class HelloWorld extends Component {
  constructor(props) {
    super(props);
    this.state = {
      message: '',
    };
  }
  // TODO: Revisit extracting this method out of the class for testing purposes
  // per conversation on PR#46
  componentDidMount() {
    superagent.get(HELLO_WORLD_URL).end((err, res) => {
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
