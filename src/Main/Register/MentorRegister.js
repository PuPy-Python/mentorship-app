import React from 'react';
import "./MentorRegister.css"
import '@progress/kendo-ui';
import { MultiSelect } from '@progress/kendo-react-dropdowns';

const interests = ["Portfolio/Code Reviews", "Job Search and Interviews",
"Industry Trends, Skills, Technologies", "Leadership, Management",
"Business, Entrepreneurship", "Career Growth"]


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
      interestFields: [],
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);

    /* Kendo MultiSelect variables*/
    this.placeholder = "Enter Interests..."
    /* End Kendo Variables*/
  }


  handleChange(event){
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
  }


  handleSubmit(event){
    /* Handles Submit when submit button is pressed */
    /* Super Agent should go here */
    alert('A name and age were submitted. \nName:  ' + this.state.portfolio + ' Age: ' + this.state.age);
    console.log(this.state.age);
    event.preventDefault();
  }

  checkPasswordMatch(){

  }


  render(){
    return(
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
          <input
            type="text"
            name="lastname"
            value={this.state.lastname}
            onChange={this.handleChange}
          />


         <p></p>
        <label htmlFor="username">Username </label>
          <input
            type="text"
            name="username"
            value={this.state.username}
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
          <input
            id="num"
            type="number"
            name="age"
            value={this.state.age}
            onChange={this.handleChange}
          />



          <p></p>

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

            </section>
      {/* **** End Section for Personal Info **** */}

      {/* Starting Section on Bio and Social Media */}
          <p></p>

          <label htmlFor="xinfo">Social Media & Info</label>
          <section id="xinfo">

          <p></p>
          <label htmlFor="bio">Bio (Maximum 500 characters)</label>
          <p></p>
          <textarea
            type="text"
            id="bio"
            name="bio"
            maxLength="500"
            value={this.state.bio}
            onChange={this.handleChange}
          />



        <p></p>
        <label htmlFor="slackHandle">Slack Handle </label>
          <input
            type="text"
            name="slackHandle"
            value={this.state.slackHandle}
            onChange={this.handleChange}
          />


      <p></p>
        <label htmlFor="linkedinURL">Linkedin URL </label>
          <input
            type="text"
            name="linkedinURL"
            value={this.state.linkedinURL}
            onChange={this.handleChange}
          />


          <p></p>
        <label htmlFor="codeRepoURL">Code Repository URL </label>
          <input
            type="text"
            name="codeRepoURL"
            value={this.state.codeRepoURL}
            onChange={this.handleChange}
          />


          <p></p>
        <label htmlFor="menteeCapacity">Mentee Capacity (allowed values 1-5)</label>
          <p></p>
          <input
            id="num"
            type="number"
            name="menteeCapacity"
            min="1"
            max="5"
            value={this.state.menteeCapacity}
            onChange={this.handleChange}
          />


          <p></p>

       </section>
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

        </form>



      </div>
    );
  }


}
export default MentorRegister;
