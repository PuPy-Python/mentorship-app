import * as profile from '../actions/profile';

const DEFAULT_STATE = {
  profile: {},
  mentor: {
    areas_of_guidance: [],
  },
  mentee: {
    areas_of_guidance: [],
  },
};

export default (state = DEFAULT_STATE, action) => {
  switch (action.type) {
    case profile.PROFILE_REQUEST:
      return state;

    case profile.PROFILE_RECEIVED:
      var new_state = { ...state };
      if (action.payload.profile) {
        new_state['profile'] = { ...action.payload.profile };
      }
      if (action.payload.mentor) {
        new_state['mentor'] = { ...action.payload.mentor };
      }
      if (action.payload.mentee) {
        new_state['mentee'] = { ...action.payload.mentee };
      }
      return new_state;

    case profile.PROFILE_FAILURE:
      return state;

    default:
      return state;
  }
};
