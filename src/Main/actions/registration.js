import { RSAA } from 'redux-api-middleware';

export const CREATE_ACCOUNT_REQUEST = '@@jwt/CREATE_ACCOUNT_REQUEST';
export const CREATE_ACCOUNT_SUCCESS = '@@jwt/CREATE_ACCOUNT_SUCCESS';
export const CREATE_ACCOUNT_FAILURE = '@@jwt/CREATE_ACCOUNT_FAILURE';

export const createAccount = values => {
  return {
    [RSAA]: {
      endpoint: 'http://localhost:8000/api/v1/user/',
      method: 'POST',
      body: JSON.stringify(values),
      headers: { 'Content-Type': 'application/json' },
      types: [CREATE_ACCOUNT_REQUEST, CREATE_ACCOUNT_SUCCESS, CREATE_ACCOUNT_FAILURE],
    },
  };
};
