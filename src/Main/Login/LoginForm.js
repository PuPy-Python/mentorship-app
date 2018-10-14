import React, { Component } from 'react';
import { Form } from 'reactstrap';
import Button from '@material-ui/core/Button';
import { withStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import TextField from '@material-ui/core/TextField';
import puppylogo from './../../puppylogo.png';
import IconButton from '@material-ui/core/IconButton';
import InputAdornment from '@material-ui/core/InputAdornment';
import Visibility from '@material-ui/icons/Visibility';
import VisibilityOff from '@material-ui/icons/VisibilityOff';
import AccountCircle from '@material-ui/icons/AccountCircle';
import VpnKey from '@material-ui/icons/VpnKey';
import { Link } from 'react-router-dom';
import Typography from '@material-ui/core/Typography';

const styles = theme => ({
  layout: {
    width: 'auto',
    display: 'row',
    marginLeft: theme.spacing.unit * 3,
    marginRight: theme.spacing.unit * 3,
    [theme.breakpoints.up(300 + theme.spacing.unit * 3 * 2)]: {
      width: 300,
      marginLeft: 'auto',
      marginRight: 'auto',
    },
  },
});

export class LoginForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      username: '',
      password: '',
      showPassword: false,
      checkedB: false,
    };
  }

  handleInputChange = event => {
    const target = event.target;
    const value = target.type === 'checkbox' ? target.checked : target.value;
    const name = target.name;

    if (target.type === 'checkbox') {
      this.setState(state => ({ checkedB: !state.checkedB }));
    } else {
      this.setState({
        [name]: value,
      });
    }
  };

  handleClickShowPassword = () => {
    this.setState(state => ({ showPassword: !state.showPassword }));
  };
  onSubmit = event => {
    event.preventDefault();
    this.props.onSubmit(this.state.username, this.state.password);
  };

  render() {
    const errors = this.props.errors || {};
    const { classes } = this.props;
    return (
      <Form onSubmit={this.onSubmit}>
        <main className={classes.layout}>
          <img src={puppylogo} style={{ width: 300, height: 75 }} alt="puppy" />
          <br />
          <br />
          <br />
          <br />
          <TextField
            name="username"
            label="Username"
            error={errors.username}
            getRef={input => (this.primaryInput = input)}
            fullWidth
            variant="outlined"
            onChange={this.handleInputChange}
            InputProps={{
              disableUnderline: true,
              startAdornment: (
                <InputAdornment position="start">
                  <AccountCircle style={{ color: '#929699' }} />
                </InputAdornment>
              ),
              endAdornment: <InputAdornment position="end" />,
            }}
          />
          <br />
          <br />
          <br />
          <TextField
            name="password"
            label="Password"
            variant="outlined"
            error={errors.password}
            fullWidth
            type={this.state.showPassword ? 'text' : 'password'}
            onChange={this.handleInputChange}
            style={{ borderColor: '#507BFC' }}
            InputProps={{
              disableUnderline: true,
              classes: {
                input: classes.textbox,
              },
              startAdornment: (
                <InputAdornment position="start">
                  <VpnKey style={{ color: '#929699' }} />
                </InputAdornment>
              ),
              endAdornment: (
                <InputAdornment position="end">
                  <IconButton
                    aria-label="Toggle password visibility"
                    onClick={this.handleClickShowPassword}
                  >
                    {this.state.showPassword ? <VisibilityOff /> : <Visibility />}
                  </IconButton>
                </InputAdornment>
              ),
            }}
          />
          <br />
          {errors.non_field_errors ? (
            <Typography style={{ color: 'red' }}>{errors.non_field_errors}</Typography>
          ) : (
            ''
          )}
          <br />
          <br />
          <br />
          <Button
            type="submit"
            variant="raised"
            color="primary"
            style={{ width: '335px', height: '46px' }}
          >
            Login
          </Button>
          <br />
          <br />
          <Grid container size={40} fullWidth>
            <Grid item xs={4}>
              <label style={{ color: '#000000', fontSize: '12px' }}>Not a member?</label>
            </Grid>
            <Grid item xs={4} />
            <Grid item xs={4}>
              <Link to="/signup" style={{ color: '#5D8FFC', fontSize: '12px' }}>
                Register now
              </Link>
            </Grid>
          </Grid>
        </main>
      </Form>
    );
  }
}

export default withStyles(styles, { name: 'LoginForm' })(LoginForm);
