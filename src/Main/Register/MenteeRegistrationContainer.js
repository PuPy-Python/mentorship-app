import { reduxForm } from 'redux-form';

import Registration from './Registration';
import validate from './RegistrationValidation';

export default reduxForm({
  form: 'MenteeRegistration',
  initialValues: { interests: [] },
  validate,
  onSubmit: () => {
    console.log('here');
  },
})(Registration);
