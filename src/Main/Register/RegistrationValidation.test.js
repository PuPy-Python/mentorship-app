import validate from './RegistrationValidation';

describe('Registration Validation', () => {
  const optionalFields = [
    { section: 'user', field: 'first_name' },
    { section: 'user', field: 'last_name' },
    { section: 'user', field: 'years_industry_experience' },
    { section: 'profile', field: 'slack_handle' },
    { section: 'profile', field: 'linked_in_url' },
    { section: 'profile', field: 'projects_url' },
    { section: 'mentor', field: 'mentee_capacity' },
  ];

  optionalFields.forEach(({ section, field }) => {
    it(`${field} in ${section} is optional`, () => {
      expect(validate({})[section][field]).toBeUndefined();
    });
  });

  it('accountType is required', () => {
    expect(validate({}).accountType).toEqual('Required');
  });

  const requiredFields = [
    { section: 'user', field: 'username' },
    { section: 'user', field: 'email' },
    { section: 'user', field: 'password' },
    { section: 'user', field: 'confirm_password' },
    { section: 'profile', field: 'bio' },
  ];

  requiredFields.forEach(({ section, field }) => {
    it(`${field} in ${section} is required`, () => {
      expect(validate({})[section][field]).toEqual('Required');
    });
  });

  it('goals in mentee is required when accountType = mentee', () => {
    expect(validate({ accountType: 'mentee' }).mentee.goals).toEqual('Required');
  });

  it('goals in mentee is not required when accountType = mentor', () => {
    expect(validate({ accountType: 'mentor' }).mentee.goals).toBeFalsy();
  });

  it('areas_of_guidance in mentee is required when accountType = mentee', () => {
    expect(validate({ accountType: 'mentee' }).mentee.areas_of_guidance).toEqual('Required');
  });

  it('areas_of_guidance in mentee is not required when accountType = mentor', () => {
    expect(validate({ accountType: 'mentor' }).mentee.areas_of_guidance).toBeFalsy();
  });

  it('mentee_capacity in mentor is required when accountType = mentor', () => {
    expect(validate({ accountType: 'mentor' }).mentor.mentee_capacity).toEqual('Required');
  });

  it('mentee_capacity in mentor is not required when accountType = mentee', () => {
    expect(validate({ accountType: 'mentee' }).mentor.mentee_capacity).toBeFalsy();
  });

  it('areas_of_guidance in mentor is required when accountType = mentor', () => {
    expect(validate({ accountType: 'mentor' }).mentor.areas_of_guidance).toEqual('Required');
  });

  it('areas_of_guidance in mentor is not required when accountType = mentee', () => {
    expect(validate({ accountType: 'mentee' }).mentor.areas_of_guidance).toBeFalsy();
  });
});
