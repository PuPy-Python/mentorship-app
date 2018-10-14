import { RSAA } from 'redux-api-middleware';

import { API_URL } from '../../constants';

export const CREATE_ACCOUNT_REQUEST = '@@jwt/CREATE_ACCOUNT_REQUEST';
export const CREATE_ACCOUNT_SUCCESS = '@@jwt/CREATE_ACCOUNT_SUCCESS';
export const CREATE_ACCOUNT_FAILURE = '@@jwt/CREATE_ACCOUNT_FAILURE';

export const createAccount = (values, history) => {
  return {
    [RSAA]: {
      endpoint: `${API_URL}/user/`,
      method: 'POST',
      body: JSON.stringify(values),
      headers: { 'Content-Type': 'application/json' },
      types: [
        { type: CREATE_ACCOUNT_REQUEST },
        {
          type: CREATE_ACCOUNT_SUCCESS,
          payload: () => history.push('/'),
        },
        { type: CREATE_ACCOUNT_FAILURE },
      ],
    },
  };
};
