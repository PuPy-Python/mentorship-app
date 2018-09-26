import { TextField as MuiTextField } from '@material-ui/core';
import { withStyles } from '@material-ui/core/styles';
import React from 'react';

const styles = theme => ({
  textBoxRoot: {
    padding: 0,
    'label + &': {
      marginTop: theme.spacing.unit * 3,
    },
  },
  textBox: {
    borderRadius: 4,
    backgroundColor: theme.palette.common.white,
    border: '1px solid #ced4da',
    fontSize: 16,
    padding: '10px 12px',
    width: 'calc(100% - 24px)',
    transition: theme.transitions.create(['border-color', 'box-shadow']),
    '&:focus': {
      borderColor: '#507BFC',
      boxShadow: '0 0 0 0.2rem rgba(0,123,255,.25)',
    },
  },
  bootstrapFormLabel: {
    fontSize: 18,
  },
});

export const TextField = ({ input, classes, meta: { touched, error }, ...rest }) => (
  <MuiTextField
    {...input}
    error={touched && !!error}
    helperText={touched && error}
    margin="normal"
    {...rest}
    fullWidth
    InputProps={{
      disableUnderline: true,
      classes: {
        root: classes.textBoxRoot,
        input: classes.textBox,
      },
    }}
    InputLabelProps={{
      shrink: true,
      className: classes.bootstrapFormLabel,
    }}
  />
);

TextField.displayName = 'TextField';

export default withStyles(styles, { name: 'TextField' })(TextField);
