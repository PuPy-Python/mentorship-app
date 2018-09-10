import { RSAA } from 'redux-api-middleware';
import { API_URL } from '../../constants';

export const LOGIN_REQUEST = '@@jwt/LOGIN_REQUEST';
export const LOGIN_SUCCESS = '@@jwt/LOGIN_SUCCESS';
export const LOGIN_FAILURE = '@@jwt/LOGIN_FAILURE';

export const TOKEN_REQUEST = '@@jwt/TOKEN_REQUEST';
export const TOKEN_RECEIVED = '@@jwt/TOKEN_RECEIVED';
export const TOKEN_FAILURE = '@@jwt/TOKEN_FAILURE';

export const login = (username, password) => ({
  [RSAA]: {
    endpoint: `${API_URL}/token-auth/`,
    method: 'POST',
    body: JSON.stringify({
      username: username,
      password: password,
    }),
    headers: { 'Content-Type': 'application/json' },
    types: [LOGIN_REQUEST, LOGIN_SUCCESS, LOGIN_FAILURE],
  },
});

export const refreshAccessToken = token => ({
  [RSAA]: {
    endpoint: `${API_URL}/token-refresh/`,
    method: 'POST',
    body: JSON.stringify({ token: token }),
    headers: { 'Content-Type': 'application/json' },
    types: [TOKEN_REQUEST, TOKEN_RECEIVED, TOKEN_FAILURE],
  },
});
