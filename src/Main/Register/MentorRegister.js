import React from 'react';
import './MentorRegister.css';
import TextField from '@material-ui/core/TextField';

class MentorRegister extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      username: '',
      firstname: '',
      lastname: '',
      password: '',
      passwordConfirmation: '',
      slackHandle: '',
      linkedinURL: '',
      codeRepoURL: '',
      bio: '',
      menteeCapacity: 0,
      age: 0,
      email: '',
      portfolio: false,
      jobSearch: false,
      skills: false,
      leadership: false,
      business: false,
      careerGrowth: false,
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    /* Handles Changes for all Values, checkbox, number, and text */
    console.log(event.target);
    const target = event.target;
    const value = target.type === 'checkbox' ? target.checked : target.value;
    const name = target.name;
    console.log(value);
    this.setState({
      [name]: value,
    });
  }

  handleSubmit(event) {
    /* Handles Submit when submit button is pressed */

    /* Super Agent should go here */

    alert(
      'A name and age were submitted. \nName:  ' + this.state.portfolio + ' Age: ' + this.state.age
    );
    console.log(this.state.age);
    event.preventDefault();
  }

  checkPasswordMatch() {
    /* Handles password matching confirmation */
  }

  render() {
    return (
      <div>
        <h1>Registration Page for Mentor</h1>
        <form onSubmit={this.handleSubmit}>
          <label for="pinfo">Personal Information</label>
          <section id="pinfo" name="personalinfo">
            <TextField name="firstname" label="First Name" onChange={this.handleChange} />
            <TextField
              name="lastname"
              label="Last Name"
              value={this.state.lastname}
              onChange={this.handleChange}
            />
            <p />
            <label for="lastname">LastName:</label>
            <input
              type="text"
              name="lastname"
              value={this.state.lastname}
              onChange={this.handleChange}
            />

            <p />
            <label for="username">Username: </label>
            <input
              type="text"
              name="username"
              value={this.state.username}
              onChange={this.handleChange}
            />

            <p />
            <label for="email"> Email: </label>
            <input type="text" name="email" value={this.state.email} onChange={this.handleChange} />

            <p />
            <label for="age"> Age: </label>
            <input
              id="num"
              type="number"
              name="age"
              value={this.state.age}
              onChange={this.handleChange}
            />

            <p />
            <label for="password"> Password:</label>
            <input
              type="password"
              name="password"
              value={this.state.password}
              onChange={this.handleChange}
            />

            <p />
            <label for="passwordConfirmation">Password Confirmation:</label>
            <input
              type="password"
              name="passwordConfirmation"
              value={null}
              onChange={this.handleChange}
            />
          </section>
          <p />
          {/* **** End Section for Personal Info **** */}
          {/* Starting Section on Bio and Social Media */}
          <label for="xinfo">Social Media & Info</label>
          <section id="xinfo">
            <p />
            <label for="bio">Bio</label>
            <p />
            <textarea
              type="text"
              id="bio"
              name="bio"
              value={this.state.bio}
              onChange={this.handleChange}
            />

            <p />
            <label for="slackHandle">Slack Handle:</label>
            <input
              type="text"
              name="slackHandle"
              value={this.state.slackHandle}
              onChange={this.handleChange}
            />

            <p />
            <label for="linkedinURL">Linkedin URL:</label>
            <input
              type="text"
              name="linkedinURL"
              value={this.state.linkedinURL}
              onChange={this.handleChange}
            />

            <p />
            <label for="codeRepoURL">Code Repository URL:</label>
            <input
              type="text"
              name="codeRepoURL"
              value={this.state.codeRepoURL}
              onChange={this.handleChange}
            />

            <p />
            <label for="menteeCapacity">Mentee Capacity:</label>
            <input
              id="num"
              type="number"
              name="menteeCapacity"
              value={this.state.menteeCapacity}
              onChange={this.handleChange}
            />

            <p />
          </section>
          {/* Social Media Section End */}
          {/* Beginning of Interests Section */}
          <p />
          <section id="interests">
            Areas of interest
            <p />
            <label for="portfolio">Portfolio/Code Review</label>
            <input
              name="portfolio"
              type="checkbox"
              checked={this.state.portfolio}
              onChange={this.handleChange}
            />
            <p />
            <label for="jobSearch">Job Search and Interviews</label>
            <input
              name="jobSearch"
              type="checkbox"
              checked={this.state.jobSearch}
              onChange={this.handleChange}
            />
            <p />
            <label for="skills">Industry Trends, Skills, Technologies</label>
            <input
              name="skills"
              type="checkbox"
              checked={this.state.skills}
              onChange={this.handleChange}
            />
            <p />
            <label for="leadership">Leadership, Management</label>
            <input
              name="leadership"
              type="checkbox"
              checked={this.state.leadership}
              onChange={this.handleChange}
            />
            <p />
            <label for="business">Business, Entrepreneurship</label>
            <input
              name="business"
              type="checkbox"
              checked={this.state.business}
              onChange={this.handleChange}
            />
            <p />
            <label for="careerGrowth">Career Growth</label>
            <input
              name="careerGrowth"
              type="checkbox"
              checked={this.state.careerGrowth}
              onChange={this.handleChange}
            />
          </section>
          <p />
          <input id="submitButton" type="button" value="Submit" onClick={this.handleSubmit} />
        </form>
      </div>
    );
  }
}

export default MentorRegister;
