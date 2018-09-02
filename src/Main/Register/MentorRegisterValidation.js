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
  firstname,
  lastname,
  username,
  email,
  password,
  confirmPassword,
  bio,
  slackHandle,
  linkedinURL,
  codeRepoURL,
  menteeCapacity,
}) => ({
  firstname: checkTooLong(firstname, MAX_FIRST_NAME_LENGTH),
  lastname: checkTooLong(lastname, MAX_FIRST_NAME_LENGTH),
  username: checkRequired(username) || checkTooLong(username, MAX_USERNAME_LENGTH),
  email: checkRequired(email) || checkEmail(email) || checkTooLong(email, MAX_EMAIL_LENGTH),
  password: checkRequired(password) || checkTooShort(password, MIN_PASSWORD_LENGTH),
  confirmPassword: checkRequired(confirmPassword) || checkPasswordsMatching(confirmPassword, password),
  bio: checkTooLong(bio, MAX_BIO_LENGTH),
  slackHandle: checkTooLong(slackHandle, MAX_SLACK_HANDLE_LENGTH),
  linkedinURL: checkTooLong(linkedinURL, MAX_LINKEDIN_URL_LENGTH) || checkUrl(linkedinURL),
  codeRepoURL: checkTooLong(codeRepoURL, MAX_CODE_REPO_URL_LENGTH) || checkUrl(codeRepoURL),
  menteeCapacity: checkNumberBetween(menteeCapacity, 0, 5),
});
