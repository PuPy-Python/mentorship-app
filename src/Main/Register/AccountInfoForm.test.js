import React from 'react';
import { shallow } from 'enzyme';
import toJson from 'enzyme-to-json';
import Button from '@material-ui/core/Button';

import { AccountInfoForm } from './AccountInfoForm';

const defaultProps = {
  classes: {},
  goToPrevious: jest.fn(),
};

const setup = props => shallow(<AccountInfoForm {...defaultProps} {...props} />);

describe('<AccountInfoForm />', () => {
  it('renders snapshot correctly', () => {
    const wrapper = setup();

    expect(toJson(wrapper)).toMatchSnapshot();
  });

  it('clicking the back button calls the goToPrevious prop', () => {
    const wrapper = setup();
    wrapper
      .find(Button)
      .first()
      .simulate('click');

    expect(defaultProps.goToPrevious).toHaveBeenCalledTimes(1);
  });
});
