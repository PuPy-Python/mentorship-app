import React from 'react';
import ReactDOM from 'react-dom';
import createHistory from 'history/createBrowserHistory';
import { Router, Route, Switch } from 'react-router-dom';
import { Provider } from 'react-redux';

import './index.css';
import App from './App';
import PrivateRoute from './Main/containers/PrivateRoute';
import Login from './Main/containers/Login';
import configureStore from './store';
import registerServiceWorker from './registerServiceWorker';

const history = createHistory();

const store = configureStore(history);

ReactDOM.render(
  <Provider store={store}>
    <Router history={history}>
      <Switch>
        <Route exact path="/login/" component={Login} />
        <PrivateRoute path="/" component={App} />
      </Switch>
    </Router>
  </Provider>,
  document.getElementById('root')
);

registerServiceWorker();
