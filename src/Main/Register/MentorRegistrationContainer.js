import { reduxForm } from 'redux-form';

import Registration from './Registration';
import validate from './RegistrationValidation';

export default reduxForm({
  form: 'MentorRegistration',
  initialValues: { interests: [] },
  validate,
  onSubmit: () => {
    console.log('here');
  },
  isMentor: true,
})(Registration);
