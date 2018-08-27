<<<<<<< HEAD
import React, { Component } from 'react';
import "./MentorRegister.css"
=======
import React from 'react';
import "./MentorRegister.css";
import '@progress/kendo-ui';
import kendo from '@progress/kendo-ui';
import { MultiSelect } from '@progress/kendo-react-dropdowns';

const interests = ["Portfolio/Code Reviews", "Job Search and Interviews",
"Industry Trends, Skills, Technologies", "Leadership, Management",
"Business, Entrepreneurship", "Career Growth"]

>>>>>>> feature/register

class MentorRegister extends React.Component {
  constructor(props){
    super(props);
    this.state ={
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
<<<<<<< HEAD
      portfolio: false,
      jobSearch: false,
      skills: false,
      leadership: false,
      business: false,
      careerGrowth: false,
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);

=======
      interestFields: [],
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);

    /* Kendo MultiSelect variables*/
    this.placeholder = "Enter Interests..."
    /* End Kendo Variables*/
>>>>>>> feature/register
  }


  handleChange(event){
<<<<<<< HEAD
    {/* Handles Changes for all Values, checkbox, number, and text */}
    const target = event.target;
    const value = target.type === 'checkbox' ? target.checked : target.value;
    const name = target.name;
    console.log(value);
    this.setState({
      [name]: value
    });
=======
    /* Handles Changes for all Values, multiselect, number, and text */
    const target = event.target;
    const value = target.value ;
    const name = target.name;

    if(name==="interestFields"){
      this.setState({
        interestFields : [...event.target.value]
      });
    }else{
      this.setState({
        [name]: value
      });
    }
>>>>>>> feature/register
  }


  handleSubmit(event){
<<<<<<< HEAD
    {/* Handles Submit when submit button is pressed */}
    {/* Super Agent should go here */}
=======
    /* Handles Submit when submit button is pressed */
    /* Super Agent should go here */
>>>>>>> feature/register
    alert('A name and age were submitted. \nName:  ' + this.state.portfolio + ' Age: ' + this.state.age);
    console.log(this.state.age);
    event.preventDefault();
  }

  checkPasswordMatch(){
<<<<<<< HEAD
    {/*Handles password matching confirmation*/}
=======
    /*Handles password matching confirmation*/
>>>>>>> feature/register
  }


  render(){
    return(
<<<<<<< HEAD
      <div>
        <h1>Registration Page for Mentor</h1>
        <form onSubmit={this.handleSubmit}>
          <label for="pinfo">Personal Information</label>
          <section id="pinfo"name="personalinfo">

            <p></p>
        <label for="firstname">FirstName:</label>
          <input type="text"
            name="firstname"
            value={this.state.firstname}
            onChange={this.handleChange}  />


          <p></p>
        <label for="lastname">LastName:</label>
=======

      <div>
      <meta
        name="viewport"
        content="width=device-width, initial-scale=1"
      />

      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/@progress/kendo-theme-default@latest/dist/all.css"
        crossOrigin="anonymous"
      />

        <h1>Registration Page for Mentor</h1>
        <form onSubmit={this.handleSubmit}>
          <label htmlFor="pinfo">Personal Information</label>
          <section id="pinfo" name="personalinfo">

            <p></p>
        <label htmlFor="firstname">FirstName</label>
          <input type="text"
            name="firstname"
            value={this.state.firstname}
            onChange={this.handleChange}
          />


          <p></p>
        <label htmlFor="lastname">LastName </label>
>>>>>>> feature/register
          <input
            type="text"
            name="lastname"
            value={this.state.lastname}
<<<<<<< HEAD
            onChange={this.handleChange}  />


         <p></p>
        <label for="username">Username: </label>
=======
            onChange={this.handleChange}
          />


         <p></p>
        <label htmlFor="username">Username </label>
>>>>>>> feature/register
          <input
            type="text"
            name="username"
            value={this.state.username}
<<<<<<< HEAD
            onChange={this.handleChange}  />


         <p></p>
        <label for="email"> Email: </label>
          <input
            type="text"
            name="email"
            value={this.state.email}
            onChange={this.handleChange}  />


        <p></p>
        <label for="age"> Age: </label>
=======
            onChange={this.handleChange}
          />


         <p></p>
        <label htmlFor="email"> Email </label>
          <input
            type="email"
            name="email"
            required
            value={this.state.email}
            onChange={this.handleChange}
          />


        <p></p>
        <label htmlFor="age"> Age </label>
>>>>>>> feature/register
          <input
            id="num"
            type="number"
            name="age"
            value={this.state.age}
<<<<<<< HEAD
            onChange={this.handleChange}  />
=======
            onChange={this.handleChange}
          />
>>>>>>> feature/register



          <p></p>
<<<<<<< HEAD
        <label for="password"> Password:</label>
          <input
            type="password"
            name="password"
            value={this.state.password}
            onChange={this.handleChange}  />


          <p></p>
        <label for="passwordConfirmation">Password Confirmation:</label>
          <input
            type="password"
            name="passwordConfirmation"
            value={null}
            onChange={this.handleChange}  />
=======
        <label htmlFor="password"> Password </label>
          <input
            type="password"
            name="password"
            required
            value={this.state.password}
            onChange={this.handleChange}
          />


          <p></p>
        <label htmlFor="passwordConfirmation">Password Confirmation </label>
          <input
            type="password"
            name="passwordConfirmation"
            required
            value={this.state.passwordConfirmation}
            onChange={this.handleChange}
          />
>>>>>>> feature/register

            </section>
      {/* **** End Section for Personal Info **** */}

      {/* Starting Section on Bio and Social Media */}
          <p></p>
<<<<<<< HEAD
          <label for="xinfo">Social Media & Info</label>
          <section id="xinfo">

          <p></p>
          <label for="bio">Bio</label>
=======
          <label htmlFor="xinfo">Social Media & Info</label>
          <section id="xinfo">

          <p></p>
          <label htmlFor="bio">Bio (Maximum 500 characters)</label>
>>>>>>> feature/register
          <p></p>
          <textarea
            type="text"
            id="bio"
            name="bio"
<<<<<<< HEAD
            value={this.state.bio}
            onChange={this.handleChange}  />



          <p></p>
        <label for="slackHandle">Slack Handle:</label>
=======
            maxLength="500"
            value={this.state.bio}
            onChange={this.handleChange}
          />



        <p></p>
        <label htmlFor="slackHandle">Slack Handle </label>
>>>>>>> feature/register
          <input
            type="text"
            name="slackHandle"
            value={this.state.slackHandle}
<<<<<<< HEAD
            onChange={this.handleChange}  />


          <p></p>
        <label for="linkedinURL">Linkedin URL:</label>
=======
            onChange={this.handleChange}
          />


      <p></p>
        <label htmlFor="linkedinURL">Linkedin URL </label>
>>>>>>> feature/register
          <input
            type="text"
            name="linkedinURL"
            value={this.state.linkedinURL}
<<<<<<< HEAD
            onChange={this.handleChange}  />


          <p></p>
        <label for="codeRepoURL">Code Repository URL:</label>
=======
            onChange={this.handleChange}
          />


          <p></p>
        <label htmlFor="codeRepoURL">Code Repository URL </label>
>>>>>>> feature/register
          <input
            type="text"
            name="codeRepoURL"
            value={this.state.codeRepoURL}
<<<<<<< HEAD
            onChange={this.handleChange}  />


          <p></p>
        <label for="menteeCapacity">Mentee Capacity:</label>
=======
            onChange={this.handleChange}
          />


          <p></p>
        <label htmlFor="menteeCapacity">Mentee Capacity (allowed values 1-5)</label>
          <p></p>
>>>>>>> feature/register
          <input
            id="num"
            type="number"
            name="menteeCapacity"
<<<<<<< HEAD
            value={this.state.menteeCapacity}
            onChange={this.handleChange}  />
=======
            min="1"
            max="5"
            value={this.state.menteeCapacity}
            onChange={this.handleChange}
          />
>>>>>>> feature/register


          <p></p>

       </section>
<<<<<<< HEAD
       {/* Social Media Section End */}

       {/* Beginning of Interests Section */}

          <p></p>
       <section id="interests">Areas of interest
         <p></p>
         <label for="portfolio">Portfolio/Code Review</label>
         <input
            name="portfolio"
            type="checkbox"
            checked={this.state.portfolio}
            onChange={this.handleChange}  />

          <p></p>
          <label for="jobSearch">Job Search and Interviews</label>
          <input
               name="jobSearch"
               type="checkbox"
               checked={this.state.jobSearch}
               onChange={this.handleChange} />

          <p></p>
          <label for="skills">Industry Trends, Skills, Technologies</label>
          <input
               name="skills"
               type="checkbox"
               checked={this.state.skills}
               onChange={this.handleChange} />


          <p></p>
          <label for="leadership">Leadership, Management</label>
          <input
               name="leadership"
               type="checkbox"
               checked={this.state.leadership}
               onChange={this.handleChange} />

          <p></p>
          <label for="business">Business, Entrepreneurship</label>
          <input
               name="business"
               type="checkbox"
               checked={this.state.business}
               onChange={this.handleChange} />

          <p></p>
          <label for="careerGrowth">Career Growth</label>
          <input
               name="careerGrowth"
               type="checkbox"
               checked={this.state.careerGrowth}
               onChange={this.handleChange} />

        </section>


          <p></p>
        <input id="submitButton"
          type="button"
          value="Submit"
          onClick={this.handleSubmit}/>
=======
       /* Social Media Section End */

       /* Beginning of Interests Section */

       <p></p>
       <section id="interests">Areas of interest
         <p></p>

         <div className="row">
           <div className="col-xs-12 col-sm-6 example-col">
             <MultiSelect
               name="interestFields"
               data={interests}
               onChange={this.handleChange}
               value= {this.state.interestFields}
               placeholder={this.placeholder}
             />
           </div>
         </div>

        </section>
        <p></p>
        <input id="submitButton"
          type="submit"
          value="Submit"
          />
>>>>>>> feature/register

        </form>



      </div>
    );
  }


}
export default MentorRegister;
