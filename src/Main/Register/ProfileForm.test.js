import React from 'react';
import { shallow } from 'enzyme';
import toJson from 'enzyme-to-json';
import Button from '@material-ui/core/Button';

import { ProfileForm } from './ProfileForm';

const defaultProps = {
  classes: {},
  goToPrevious: jest.fn(),
  handleSubmit: jest.fn(),
  registration: {},
};

const setup = props => shallow(<ProfileForm {...defaultProps} {...props} />);

describe('<ProfileForm />', () => {
  it('renders snapshot correctly', () => {
    const wrapper = setup();

    expect(toJson(wrapper)).toMatchSnapshot();
  });

  it('renders the correct title when accountType = mentor', () => {
    const wrapper = setup({ accountType: 'mentor' });

    expect(wrapper.findWhere(n => n.text() === 'MENTEE')).toHaveLength(0);
    expect(wrapper.findWhere(n => n.text() === 'MENTOR')).toHaveLength(1);
  });

  it('renders the correct title when accountType = mentee', () => {
    const wrapper = setup({ accountType: 'mentee' });

    expect(wrapper.findWhere(n => n.text() === 'MENTEE')).toHaveLength(1);
    expect(wrapper.findWhere(n => n.text() === 'MENTOR')).toHaveLength(0);
  });

  it('renders mentee capacity when accountType = mentor', () => {
    const wrapper = setup({ accountType: 'mentor' });

    expect(wrapper.find('[name="mentee_capacity"]')).toHaveLength(1);
  });

  it('does not render mentee capacity when accountType = mentee', () => {
    const wrapper = setup({ accountType: 'mentee' });

    expect(wrapper.find('[name="menteeCapacity"]')).toHaveLength(0);
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
