import React from 'react';
import ReactDOM from 'react-dom';
import createHistory from 'history/createBrowserHistory';
import { Router, Route, Switch } from 'react-router-dom';
import { Provider } from 'react-redux';
import mainTheme from './Main/theme/mainTheme';
import MuiThemeProvider from '@material-ui/core/styles/MuiThemeProvider';
import './index.css';
import App from './App';
import Login from './Main/containers/Login';
import configureStore from './store';
import registerServiceWorker from './registerServiceWorker';

const history = createHistory();

const store = configureStore(history);

ReactDOM.render(
  <Provider store={store}>
    <Router history={history}>
      <MuiThemeProvider theme={mainTheme}>
        <Switch>
          <Route exact path="/login/" component={Login} />
          <Route path="/" component={App} />
        </Switch>
      </MuiThemeProvider>
    </Router>
  </Provider>,
  document.getElementById('root')
);

registerServiceWorker();
