import React from 'react';
import { formValueSelector, reduxForm, Field } from 'redux-form';
import { compose } from 'recompose';
import { connect } from 'react-redux';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';

import RadioGroup from '../forms/RadioGroup';
import validate from './RegistrationValidation';
import TextField from '../forms/TextField';
import SelectField from '../forms/SelectField';

const experience = [
  { label: '0-1', value: 'entry' },
  { label: '1-3', value: 'junior' },
  { label: '3-7', value: 'intermediate' },
  { label: '7+', value: 'senior' },
];

const interests = [
  { label: 'Portfolio/Code Review', value: 'portfolio' },
  { label: 'Job Search and Interviews', value: 'jobSearch' },
  { label: 'Industry Trends, Skills, Technologies', value: 'skills' },
  { label: 'Leadership, Management', value: 'leadership' },
  { label: 'Business, Entrepreneurship', value: 'business' },
  { label: 'Career Growth', value: 'careerGrowth' },
];

export const ProfileForm = ({ handleSubmit, classes, goToPrevious, accountType = '' }) => (
  <form onSubmit={handleSubmit} noValidate>
    <Typography variant="subheading" color="secondary" gutterBottom>
      CREATE YOUR {accountType.toUpperCase()} PROFILE
    </Typography>
    <Typography variant="subheading" color="secondary" gutterBottom>
      _____
    </Typography>

    <Field name="slackHandle" label="Slack Handle" component={TextField} />
    <Field name="linkedinURL" label="Linkedin URL" component={TextField} />
    <Field name="codeRepoURL" label="Code Repository URL" component={TextField} />
    <Field name="bio" label="Bio" multiline rows="8" component={TextField} />
    <Field name="goals" label="Goals" multiline rows="5" component={TextField} />
    {accountType === 'Mentor' && (
      <Field name="menteeCapacity" label="Mentee Capacity" type="number" component={TextField} />
    )}
    <Field
      name="yearsOfExperience"
      label="Years of Industry Experience"
      component={RadioGroup}
      source={experience}
    />
    <Field name="interests" label="Interests" multiple component={SelectField} items={interests} />

    <Button
      variant="raised"
      color="secondary"
      size="large"
      className={classes.button}
      onClick={goToPrevious}
    >
      BACK
    </Button>
    <Button variant="raised" type="submit" color="primary" size="large" className={classes.button}>
      CONTINUE
    </Button>
  </form>
);

ProfileForm.displayName = 'ProfileForm';

const selector = formValueSelector('registration');

const mapStateToProps = state => ({
  accountType: selector(state, 'accountType'),
});

export default compose(
  connect(mapStateToProps),
  reduxForm({
    form: 'registration',
    destroyOnUnmount: false,
    forceUnregisterOnUnmount: true,
    validate,
    initialValues: {
      interests: [],
    },
    onSubmit: () => {
      console.log('not yet implemented');
    },
  })
)(ProfileForm);
