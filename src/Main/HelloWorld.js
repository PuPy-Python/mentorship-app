import React, { Component } from 'react';
import superagent from 'superagent';

const __API_HOST__ = process.env.REACT_APP_API_HOST || 'http://localhost:8000';

class HelloWorld extends Component {
  constructor(props) {
    super(props);
    this.state = {
      message: '',
    }
  }

  componentDidMount() {
    superagent
    .get(`${__API_HOST__}/api/v1/helloworld/`)
    .end( (err, res) => {
      let message = res.body['message'];
      this.setState({
        message:message
      });
    });
  }

  render() {
    return (
      <div className="HelloWorld">
        <p>
          {this.state.message}
        </p>
      </div>
    );
  }
}

export default HelloWorld;
