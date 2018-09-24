import React from 'react';
import { Field } from 'redux-form';
import { withStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';
import RadioGroup from '../forms/RadioGroup';
import TextField from '../forms/TextField';
import SelectField from '../forms/SelectField';

const styles = {
  form: {
    '@media (min-width: 1024px)': {
      width: '675px',
    },
    margin: 'auto',
    padding: '20px',
  },
};

const interests = [
  { label: 'Portfolio/Code Review', value: 'portfolio' },
  { label: 'Job Search and Interviews', value: 'jobSearch' },
  { label: 'Industry Trends, Skills, Technologies', value: 'skills' },
  { label: 'Leadership, Management', value: 'leadership' },
  { label: 'Business, Entrepreneurship', value: 'business' },
  { label: 'Career Growth', value: 'careerGrowth' },
];

export const Registration = ({ handleSubmit, classes, isMentor }) => {
  return (
    <div className={classes.form}>
      <h1>{(isMentor ? 'Mentor' : 'Mentee') + ' Registration'}</h1>
      <form onSubmit={handleSubmit} noValidate>
        <label htmlFor="pinfo">Personal Information</label>
        <section id="pinfo" name="personalinfo">
          <Field name="firstname" label="First Name" component={TextField} />
          <Field name="lastname" label="Last Name" component={TextField} />
          <Field name="username" label="Username" component={TextField} required />
          <Field name="email" label="E-mail" component={TextField} required />
          <Field name="password" label="Password" type="password" component={TextField} required />
          <Field
            name="confirmPassword"
            label="Confirm Password"
            type="password"
            component={TextField}
            required
          />
        </section>
        <br />
        <label htmlFor="xinfo">Social Media & Info</label>
        <section id="xinfo">
          <Field name="bio" label="Bio" multiline rows="8" component={TextField} />
          <Field name="goals" label="Goals" multiline rows="5" component={TextField} />
          <p />
          <Field
            name="yearsOfExperience"
            label="Years of Industry Experience"
            component={RadioGroup}
            source={[
              { value: 'entry', label: '0' },
              { value: 'junior', label: '1-2' },
              { value: 'intermediate', label: '3-6' },
              { value: 'senior', label: '7+' },
            ]}
          />

          <Field name="slackHandle" label="Slack Handle" component={TextField} />
          <Field name="linkedinURL" label="Linkedin URL" component={TextField} />
          <Field name="codeRepoURL" label="Code Repository URL" component={TextField} />
          {isMentor && (
            <Field
              name="menteeCapacity"
              label="Mentee Capacity"
              type="number"
              component={TextField}
            />
          )}
        </section>
        <br />
        <label htmlFor="interests">Areas of {isMentor ? 'Expertise' : 'Interests'}</label>
        <section id="interests">
          <Field
            name="interests"
            label="Interests"
            multiple
            component={SelectField}
            items={interests}
          />
        </section>
        <br />
        <Button variant="contained" type="submit" color="primary">
          Submit
        </Button>
      </form>
    </div>
  );
};

export default withStyles(styles, { name: 'Registration' })(Registration);
