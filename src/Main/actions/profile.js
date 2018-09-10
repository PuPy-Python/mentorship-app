import { RSAA } from 'redux-api-middleware';
import { API_URL } from '../../constants';

export const PROFILE_REQUEST = 'PROFILE_REQUEST';
export const PROFILE_RECEIVED = 'PROFILE_RECEIVED';
export const PROFILE_FAILURE = 'PROFILE_FAILURE';

export const getProfile = (token, username) => ({
  [RSAA]: {
    endpoint: `${API_URL}/user/${username}`,
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `JWT ${token}`,
    },
    types: [PROFILE_REQUEST, PROFILE_RECEIVED, PROFILE_FAILURE],
  },
});
