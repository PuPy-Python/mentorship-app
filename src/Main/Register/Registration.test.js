import React from 'react';
import { shallow } from 'enzyme';

import { Registration } from './Registration';
import AccountTypeForm from './AccountTypeForm';
import AccountInfoForm from './AccountInfoForm';
import ProfileForm from './ProfileForm';

const defaultProps = {
  classes: {},
};

const setup = props => shallow(<Registration {...defaultProps} {...props} />);

describe('<Registration />', () => {
  it('renders AccountTypeForm by default', () => {
    const wrapper = setup();

    expect(wrapper.find(AccountTypeForm)).toHaveLength(1);
    expect(wrapper.find(AccountInfoForm)).toHaveLength(0);
    expect(wrapper.find(ProfileForm)).toHaveLength(0);
  });

  it('renders AccountTypeForm when activeStep = 0', () => {
    const wrapper = setup({ activeStep: 0 });

    expect(wrapper.find(AccountTypeForm)).toHaveLength(1);
    expect(wrapper.find(AccountInfoForm)).toHaveLength(0);
    expect(wrapper.find(ProfileForm)).toHaveLength(0);
  });

  it('renders AccountInfoForm when activeStep = 1', () => {
    const wrapper = setup();
    wrapper.setState({ activeStep: 1 });

    expect(wrapper.find(AccountTypeForm)).toHaveLength(0);
    expect(wrapper.find(AccountInfoForm)).toHaveLength(1);
    expect(wrapper.find(ProfileForm)).toHaveLength(0);
  });

  it('renders ProfileForm when activeStep = 2', () => {
    const wrapper = setup();
    wrapper.setState({ activeStep: 2 });

    expect(wrapper.find(AccountTypeForm)).toHaveLength(0);
    expect(wrapper.find(AccountInfoForm)).toHaveLength(0);
    expect(wrapper.find(ProfileForm)).toHaveLength(1);
  });
});
