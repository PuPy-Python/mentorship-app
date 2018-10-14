import React from 'react';
import { formValueSelector, reduxForm, Field, FormSection } from 'redux-form';
import { compose } from 'recompose';
import { connect } from 'react-redux';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import { withRouter } from 'react-router-dom';

import RadioGroup from '../forms/RadioGroup';
import validate from './RegistrationValidation';
import TextField from '../forms/TextField';
import SelectField from '../forms/SelectField';
import { createAccount } from '../actions/registration';

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

export const ProfileForm = ({
  handleSubmit,
  createAccount,
  classes,
  goToPrevious,
  accountType = 'mentee',
  history,
  registration,
}) => (
  <form onSubmit={handleSubmit(values => createAccount(values, history))} noValidate>
    <Typography variant="subheading" color="secondary" gutterBottom>
      CREATE YOUR {accountType.toUpperCase()} PROFILE
    </Typography>
    <Typography variant="subheading" color="secondary" gutterBottom>
      _____
    </Typography>

    <FormSection name="profile">
      <Field name="slack_handle" label="Slack Handle" component={TextField} />
      <Field name="linked_in_url" label="Linkedin URL" component={TextField} />
      <Field name="projects_url" label="Code Repository URL" component={TextField} />
      <Field name="bio" label="Bio" multiline rows="8" component={TextField} required />
    </FormSection>
    <FormSection name={accountType}>
      {(accountType === 'mentee' && (
        <Field name="goals" label="Goals" multiline rows="5" component={TextField} required />
      )) ||
        (accountType === 'mentor' && (
          <Field
            name="mentee_capacity"
            label="Mentee Capacity"
            type="number"
            component={TextField}
            required
          />
        ))}
    </FormSection>
    <FormSection name="profile">
      <Field
        name="years_industry_experience"
        label="Years of Industry Experience"
        component={RadioGroup}
        source={experience}
      />
    </FormSection>
    <FormSection name={accountType}>
      <Field
        name="areas_of_guidance"
        label="Areas of Guidance"
        multiple
        component={SelectField}
        items={interests}
        required
      />
    </FormSection>

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
    {registration.user && (
      <Typography style={{ color: 'red' }}>
        {Object.keys(registration.user).map(key => registration.user[key])}
      </Typography>
    )}
    {registration.profile && (
      <Typography style={{ color: 'red' }}>
        {Object.keys(registration.profile).map(key => registration.profile[key])}
      </Typography>
    )}
  </form>
);

ProfileForm.displayName = 'ProfileForm';

const selector = formValueSelector('registration');

const mapStateToProps = state => ({
  accountType: selector(state, 'accountType'),
  registration: state.registration,
});

const mapDispatchToProps = { createAccount };

export default compose(
  connect(
    mapStateToProps,
    mapDispatchToProps
  ),
  withRouter,
  reduxForm({
    form: 'registration',
    destroyOnUnmount: false,
    forceUnregisterOnUnmount: true,
    validate,
  })
)(ProfileForm);
