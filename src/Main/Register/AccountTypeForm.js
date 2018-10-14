import React from 'react';
import { reduxForm, Field } from 'redux-form';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import RadioGroup from '../forms/RadioGroup';
import validate from './RegistrationValidation';

const accountTypes = [{ label: 'Mentee', value: 'mentee' }, { label: 'Mentor', value: 'mentor' }];

export const AccountTypeForm = ({ handleSubmit, classes }) => (
  <form onSubmit={handleSubmit} noValidate>
    <Typography variant="subheading" color="secondary" gutterBottom>
      CHOOSE ACCOUNT TYPE
    </Typography>
    <Typography variant="subheading" color="secondary" gutterBottom>
      _____
    </Typography>

    <Field name="accountType" component={RadioGroup} source={accountTypes} />

    <Button
      variant="raised"
      isHidden="true"
      color="secondary"
      size="large"
      className={classes.button}
      disabled
    >
      BACK
    </Button>

    <Button variant="raised" type="submit" color="primary" size="large" className={classes.button}>
      CONTINUE
    </Button>
  </form>
);

AccountTypeForm.displayName = 'AccountTypeForm';

export default reduxForm({
  form: 'registration',
  destroyOnUnmount: false,
  forceUnregisterOnUnmount: true,
  validate,
  initialValues: {
    accountType: 'mentee',
  },
})(AccountTypeForm);
