export const checkRequired = value => {
  if (!value || (typeof value === 'string' && !value.trim()) || value.length === 0) {
    return 'Required';
  }
};

export const checkNormalSymbolsOnly = value => {
  if (!/^[\w\s]+$/i.test(value)) {
    return 'Must contain only valid characters';
  }
};

export const checkTooLong = (value, length) => {
  if (value && value.length > length) {
    return `Must be ${length} characters or less`;
  }
};

export const checkTooShort = (value, length) => {
  if (!value || value.length < length) {
    return `Must be ${length} characters or more`;
  }
};

export const checkUrl = value => {
  if (
    value &&
    !/^(http:\/\/|https:\/\/)[a-z0-9]+([-.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?([^\s]+)?$/.test(
      value
    )
  ) {
    return 'Must be a valid URL';
  }
};

export const checkEmail = value => {
  if (value && !/^[a-zA-Z0-9.!#$%&’*+/=?^_{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$/.test(value)) {
    return 'Must be a valid email';
  }
};

export const checkPasswordsMatching = (value1, value2) => {
  if (value1 !== value2) {
    return 'Passwords must match';
  }
};

export const checkNumberBetween = (value, min, max) => {
  if (
    (value && !/^[0-9]+$/i.test(value)) ||
    parseInt(value, 10) < min ||
    parseInt(value, 10) > max
  ) {
    return `Must be between ${min} and ${max}`;
  }
};
