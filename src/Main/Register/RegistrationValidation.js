import {
  checkRequired,
  checkTooLong,
  checkTooShort,
  checkUrl,
  checkEmail,
  checkPasswordsMatching,
  checkNumberBetween,
} from '../forms/validation';

export const MAX_FIRST_NAME_LENGTH = 30;
export const MAX_LAST_NAME_LENGTH = 30;
export const MAX_USERNAME_LENGTH = 150;
export const MAX_EMAIL_LENGTH = 75;
export const MIN_PASSWORD_LENGTH = 8;
export const MAX_BIO_LENGTH = 500;
export const MAX_SLACK_HANDLE_LENGTH = 40;
export const MAX_LINKEDIN_URL_LENGTH = 200;
export const MAX_CODE_REPO_URL_LENGTH = 200;

export default ({
  accountType,
  user: { firstname, lastname, username, email, password, confirm_password } = {},
  profile: { bio, slack_handle, linked_in_url, projects_url } = {},
  mentor: { mentee_capacity, areas_of_guidance: mentor_areas_of_guidance } = {},
  mentee: { goals, areas_of_guidance: mentee_areas_of_guidance } = {},
}) => ({
  accountType: checkRequired(accountType),
  user: {
    firstname: checkTooLong(firstname, MAX_FIRST_NAME_LENGTH),
    lastname: checkTooLong(lastname, MAX_FIRST_NAME_LENGTH),
    username: checkRequired(username) || checkTooLong(username, MAX_USERNAME_LENGTH),
    email: checkRequired(email) || checkEmail(email) || checkTooLong(email, MAX_EMAIL_LENGTH),
    password: checkRequired(password) || checkTooShort(password, MIN_PASSWORD_LENGTH),
    confirm_password:
      checkRequired(confirm_password) || checkPasswordsMatching(confirm_password, password),
  },
  profile: {
    bio: checkRequired(bio) || checkTooLong(bio, MAX_BIO_LENGTH),
    slackHandle: checkTooLong(slack_handle, MAX_SLACK_HANDLE_LENGTH),
    linkedinURL: checkTooLong(linked_in_url, MAX_LINKEDIN_URL_LENGTH) || checkUrl(linked_in_url),
    codeRepoURL: checkTooLong(projects_url, MAX_CODE_REPO_URL_LENGTH) || checkUrl(projects_url),
  },
  mentor: {
    mentee_capacity:
      (accountType === 'mentor' && checkRequired(mentee_capacity)) ||
      checkNumberBetween(mentee_capacity, 0, 5),
    areas_of_guidance: accountType === 'mentor' && checkRequired(mentor_areas_of_guidance),
  },
  mentee: {
    goals: accountType === 'mentee' && checkRequired(goals),
    areas_of_guidance: accountType === 'mentee' && checkRequired(mentee_areas_of_guidance),
  },
});
