import React from 'react';
import ReactDOM from 'react-dom';
import { App } from './App';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<App fetchMessage={jest.fn()} />, div);
  ReactDOM.unmountComponentAtNode(div);
});
