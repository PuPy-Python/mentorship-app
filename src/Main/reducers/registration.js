import { CREATE_ACCOUNT_FAILURE } from '../actions/registration';

export default (state = {}, action) => {
  switch (action.type) {
    case CREATE_ACCOUNT_FAILURE:
      return action.payload.response;

    default:
      return state;
  }
};
