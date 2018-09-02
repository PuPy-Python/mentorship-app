import { reduxForm } from 'redux-form';

import MentorRegister from './MentorRegister';
import validate from './MentorRegisterValidation';

export default reduxForm({ form: 'MentorRegister', initialValues: { interests: [] }, validate })(
  MentorRegister
);
