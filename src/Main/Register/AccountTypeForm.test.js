import React from 'react';
import { shallow } from 'enzyme';
import toJson from 'enzyme-to-json';
import Button from '@material-ui/core/Button';

import { AccountTypeForm } from './AccountTypeForm';

const defaultProps = {
  classes: {},
};

const setup = props => shallow(<AccountTypeForm {...defaultProps} {...props} />);

describe('<AccountTypeForm />', () => {
  it('renders snapshot correctly', () => {
    const wrapper = setup();

    expect(toJson(wrapper)).toMatchSnapshot();
  });

  it('has a disabled back button', () => {
    const wrapper = setup();

    expect(
      wrapper
        .find(Button)
        .first()
        .is('[disabled]')
    ).toBe(true);
  });
});
