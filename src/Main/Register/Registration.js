import React from 'react';
import { withStyles } from '@material-ui/core/styles';
import Stepper from '@material-ui/core/Stepper';
import Step from '@material-ui/core/Step';
import StepLabel from '@material-ui/core/StepLabel';
import AccountTypeForm from './AccountTypeForm';
import AccountInfoForm from './AccountInfoForm';
import ProfileForm from './ProfileForm';

const styles = {
  form: {
    '@media (min-width: 1024px)': {
      width: '675px',
    },
    margin: 'auto',
    padding: '20px',
  },
  button: {
    margin: 15,
  },
};

export class Registration extends React.Component {
  constructor(props) {
    super(props);
    this.goToNext = this.goToNext.bind(this);
    this.goToPrevious = this.goToPrevious.bind(this);
    this.state = {
      activeStep: 0,
    };
  }

  goToNext() {
    this.setState({ activeStep: this.state.activeStep + 1 });
  }

  goToPrevious() {
    this.setState({ activeStep: this.state.activeStep - 1 });
  }

  render() {
    const { classes } = this.props;
    const { activeStep } = this.state;

    return (
      <div className={classes.form}>
        <Stepper activeStep={activeStep} alternativeLabel>
          <Step>
            <StepLabel>Account Type</StepLabel>
          </Step>
          <Step>
            <StepLabel>Account Info</StepLabel>
          </Step>
          <Step>
            <StepLabel>Profile</StepLabel>
          </Step>
        </Stepper>
        <br />
        {activeStep === 0 && <AccountTypeForm onSubmit={this.goToNext} classes={classes} />}

        {activeStep === 1 && (
          <AccountInfoForm
            onSubmit={this.goToNext}
            goToPrevious={this.goToPrevious}
            classes={classes}
          />
        )}

        {activeStep === 2 && <ProfileForm goToPrevious={this.goToPrevious} classes={classes} />}
      </div>
    );
  }
}

export default withStyles(styles, { name: 'Registration' })(Registration);
