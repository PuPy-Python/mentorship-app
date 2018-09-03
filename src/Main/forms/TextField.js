import { TextField as MuiTextField } from '@material-ui/core';
import { withStyles } from '@material-ui/core/styles';
import React from 'react';

const styles = {
  width: {},
};

export const TextField = ({ input, classes, meta: { touched, error }, ...rest }) => (
  <MuiTextField
    {...input}
    error={touched && !!error}
    helperText={touched && error}
    margin="normal"
    {...rest}
    fullWidth
    className={classes.width}
  />
);

TextField.displayName = 'TextField';

export default withStyles(styles, { name: 'TextField' })(TextField);
