import React from 'react';
import { reduxForm, Field, FormSection } from 'redux-form';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import validate from './RegistrationValidation';
import TextField from '../forms/TextField';

export const AccountInfoForm = ({ handleSubmit, classes, goToPrevious }) => (
  <form onSubmit={handleSubmit} noValidate>
    <Typography variant="subheading" color="secondary" gutterBottom>
      FILL IN ACCOUNT INFO
    </Typography>
    <Typography variant="subheading" color="secondary" gutterBottom>
      _____
    </Typography>

    <FormSection name="user">
      <Field name="first_name" label="First Name" component={TextField} />
      <Field name="last_name" label="Last Name" component={TextField} />
      <Field name="username" label="Username" component={TextField} required />
      <Field name="email" label="E-mail" component={TextField} required />
      <Field name="password" label="Password" type="password" component={TextField} required />
      <Field
        name="confirm_password"
        label="Confirm Password"
        type="password"
        component={TextField}
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
    <Button
      variant="contained"
      type="submit"
      color="primary"
      size="large"
      className={classes.button}
    >
      CONTINUE
    </Button>
  </form>
);

AccountInfoForm.displayName = 'AccountInfoForm';

export default reduxForm({
  form: 'registration',
  destroyOnUnmount: false,
  forceUnregisterOnUnmount: true,
  validate,
})(AccountInfoForm);
