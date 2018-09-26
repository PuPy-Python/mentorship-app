import validate from './RegistrationValidation';

describe('Registration Validation', () => {
  const optionalFields = [
    'firstname',
    'lastname',
    'bio',
    'slackHandle',
    'linkedinURL',
    'codeRepoURL',
    'menteeCapacity',
  ];

  optionalFields.forEach(field => {
    it(`${field} is optional`, () => {
      expect(validate({})[field]).toBeUndefined();
    });
  });

  const requiredFields = ['accountType', 'username', 'email', 'password', 'confirmPassword'];

  requiredFields.forEach(field => {
    it(`${field} is required`, () => {
      expect(validate({})[field]).toEqual('Required');
    });
  });
});
