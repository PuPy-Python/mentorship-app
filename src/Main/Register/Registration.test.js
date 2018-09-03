import React from 'react';
import { shallow } from 'enzyme';

import { Registration } from './Registration';

const defaultProps = {
  classes: {},
};

const setup = props => shallow(<Registration {...defaultProps} {...props} />);

describe('<Registration />', () => {
  it('renders snapshot correctly when "isMentor" is undefined', () => {
    const wrapper = setup();

    expect(wrapper.find('[name="menteeCapacity"]')).toHaveLength(0);
  });

  it('renders snapshot correctly when "isMentor" is true', () => {
    const wrapper = setup({ isMentor: true });

    expect(wrapper.find('[name="menteeCapacity"]')).toHaveLength(1);
  });
});
