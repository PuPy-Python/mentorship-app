import {
  checkRequired,
  checkTooLong,
  checkTooShort,
  checkUrl,
  checkEmail,
  checkPasswordsMatching,
  checkNumberBetween,
} from './validation';

describe('checkRequired', () => {
  const validInputCases = ['some text', '  trim me   ', { fooObject: 'bar' }, 20, [1]];

  const invalidInputCases = ['', ' ', ' \n ', '   \t  ', [], null, undefined];

  validInputCases.forEach(validInput => {
    it(`returns undefined for valid input: "${validInput}"`, () => {
      const result = checkRequired(validInput);

      expect(result).toBeUndefined();
    });
  });

  invalidInputCases.forEach(invalidInput => {
    it(`renders message for invalid input: "${invalidInput}"`, () => {
      const result = checkRequired(invalidInput);

      expect(result).toEqual('Required');
    });
  });
});

describe('checkTooLong', () => {
  const testcases = [
    { value: '7 chars', maxLength: 6, expectError: true },
    { value: '7 chars', maxLength: 7, expectError: false },
    { value: '7 chars', maxLength: 8, expectError: false },
    { value: 'Test Text', maxLength: 5, expectError: true },
    { value: '', maxLength: 0, expectError: false },
    { value: '', maxLength: 5, expectError: false },
    { value: [], maxLength: 5, expectError: false },
    { value: [1, 2, 3], maxLength: 2, expectError: true },
  ];
  testcases.forEach(({ value, maxLength, expectError }) => {
    it(`handles validation for input: ${value}, maxLength: ${maxLength}`, () => {
      const result = checkTooLong(value, maxLength);

      if (expectError) {
        expect(result).toEqual(`Must be ${maxLength} characters or less`);
      } else {
        expect(result).toBeUndefined();
      }
    });
  });
});

describe('checkTooShort', () => {
  const testcases = [
    { value: '7 chars', minLength: 6, expectError: false },
    { value: '7 chars', minLength: 7, expectError: false },
    { value: '7 chars', minLength: 8, expectError: true },
    { value: 'Test Text', minLength: 5, expectError: false },
    { value: '', minLength: 1, expectError: true },
    { value: '', minLength: 5, expectError: true },
    { value: [], minLength: 5, expectError: true },
    { value: [1, 2, 3], minLength: 2, expectError: false },
  ];
  testcases.forEach(({ value, minLength, expectError }) => {
    it(`handles validation for input: ${value}, minLength: ${minLength}`, () => {
      const result = checkTooShort(value, minLength);

      if (expectError) {
        expect(result).toEqual(`Must be ${minLength} characters or more`);
      } else {
        expect(result).toBeUndefined();
      }
    });
  });
});

describe('checkUrl', () => {
  const validUrlCases = [
    'http://www.example.com',
    'http://www.example.com/this/is!/A/Test22(?-*)/',
    'https://www.example.com/123123/?hello',
    'https://example.com/hello-world!',
    'https://yes.example.com/',
    'https://yes.foo.bar.fizz.buzz.dinosaur.derp.doo.dee.bee.ooo.example.com/',
    '',
    null,
    undefined,
  ];

  const invalidUrlCases = [
    '   \t  ',
    'http://www. example.com',
    'h ttp://www.example.com',
    'http://ww w.example.com',
    'http://www.example.com /hello',
    'www.example.com',
    'http://w ww.!a;sdasdksd.com /09h09h2',
    'https://example.com/hello-     world!',
  ];

  validUrlCases.forEach(validUrl => {
    it(`returns undefined for valid input: "${validUrl}"`, () => {
      const result = checkUrl(validUrl);

      expect(result).toBeUndefined();
    });
  });

  invalidUrlCases.forEach(invalidUrl => {
    it(`renders message for invalid input: "${invalidUrl}"`, () => {
      const result = checkUrl(invalidUrl);

      expect(result).toEqual('Must be a valid URL');
    });
  });
});

describe('checkEmail', () => {
  const validEmailCases = [
    'foo@example.com',
    'FOO@example.com',
    'foo.bar@example.co.jp',
    'foo+bar@baz.org',
    undefined,
    null,
  ];

  const invalidEmailCases = ['foo', 'foo@com', 'foo@.com', '@example.com', ' '];

  validEmailCases.forEach(validEmail => {
    it(`returns undefined for valid input: "${validEmail}"`, () => {
      const result = checkEmail(validEmail);

      expect(result).toBeUndefined();
    });
  });

  invalidEmailCases.forEach(invalidEmail => {
    it(`renders message for invalid input: "${invalidEmail}"`, () => {
      const result = checkEmail(invalidEmail);

      expect(result).toEqual('Must be a valid email');
    });
  });
});

describe('checkPasswordsMatching', () => {
  const validCases = [
    { value1: 'a', value2: 'a' },
    { value1: 'abcd', value2: 'abcd' },
    { value1: '!@#$%^&*()1234567890', value2: '!@#$%^&*()1234567890' },
    { value1: 'hunter2', value2: 'hunter2' },
  ];

  const invalidCases = [
    { value1: 'a', value2: 'b' },
    { value1: 'a', value2: 'b ' },
    { value1: 'abcd', value2: 'abcde' },
    { value1: '!@#$%^&*()1234567890', value2: '1234567890!@#$%^&*()' },
    { value1: 'hunter2', value2: 'hunter3' },
  ];

  validCases.forEach(({ value1, value2 }) => {
    it(`returns undefined for valid input: "${value1}" and "${value2}"`, () => {
      const result = checkPasswordsMatching(value1, value2);

      expect(result).toBeUndefined();
    });
  });

  invalidCases.forEach(({ value1, value2 }) => {
    it(`renders message for invalid input: "${value1}" and "${value2}"`, () => {
      const result = checkPasswordsMatching(value1, value2);

      expect(result).toEqual('Passwords must match');
    });
  });
});

describe('checkNumberBetween', () => {
  const validCases = [
    { value: 1, min: 1, max: 1 },
    { value: 0, min: 0, max: 10 },
    { value: 10, min: 0, max: 10 },
    { value: 5, min: 0, max: 10 },
  ];

  const invalidCases = [
    { value: 0, min: 1, max: 1 },
    { value: -1, min: 1, max: 1 },
    { value: 2, min: 1, max: 1 },
    { value: 0, min: 1, max: 10 },
    { value: 10, min: 1, max: 9 },
  ];

  validCases.forEach(({ value, min, max }) => {
    it(`returns undefined for valid input: value="${value}", min="${min}" and max="${max}"`, () => {
      const result = checkNumberBetween(value, min, max);

      expect(result).toBeUndefined();
    });
  });

  invalidCases.forEach(({ value, min, max }) => {
    it(`renders message for invalid input: value="${value}", min="${min}" and max="${max}"`, () => {
      const result = checkNumberBetween(value, min, max);

      expect(result).toEqual(`Must be between ${min} and ${max}`);
    });
  });
});
