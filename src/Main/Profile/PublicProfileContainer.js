import React, { Component } from 'react';
import { connect } from 'react-redux';
import { getProfile } from '../actions/profile';
import AboutCard from './AboutCard/AboutCard';
import MentorCard from './MentorCard/MentorCard';
import MenteeCard from './MenteeCard/MenteeCard';

class PublicProfileContainer extends Component {
  componentDidMount() {
    let username = this.props.match.params.username || '';
    this.props.getProfile(this.props.token, username);
  }
  render() {
    return (
      <div className="PublicProfileContainer">
        <p>{this.props.match.params.username || this.props.username}</p>
        <AboutCard />
        <MentorCard />
        <MenteeCard />
      </div>
    );
  }
}

const mapStateToProps = state => ({
  token: state.auth.access.token,
  username: state.auth.access.username,
});

const mapDispatchToProps = dispatch => ({
  getProfile: (token, username) => dispatch(getProfile(token, username)),
});

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(PublicProfileContainer);
