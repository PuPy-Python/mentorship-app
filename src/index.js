import React from 'react';
import ReactDOM from 'react-dom';
import createHistory from 'history/createBrowserHistory';
import { Router } from 'react-router-dom';
import { Provider } from 'react-redux';
import mainTheme from './Main/theme/mainTheme';
import MuiThemeProvider from '@material-ui/core/styles/MuiThemeProvider';
import './index.css';
import App from './App';
import configureStore from './store';
import registerServiceWorker from './registerServiceWorker';

const history = createHistory();

const store = configureStore(history);

ReactDOM.render(
  <Provider store={store}>
    <MuiThemeProvider theme={mainTheme}>
      <Router history={history}>
        <App />
      </Router>
    </MuiThemeProvider>
  </Provider>,
  document.getElementById('root')
);

registerServiceWorker();
