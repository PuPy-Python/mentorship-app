import { withStyles } from '@material-ui/core/styles';
import FormControl from '@material-ui/core/FormControl';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import FormLabel from '@material-ui/core/FormLabel';
import PropTypes from 'prop-types';
import Radio from '@material-ui/core/Radio';
import RadioButtonGroup from '@material-ui/core/RadioGroup';
import React from 'react';
import FormHelperText from '@material-ui/core/FormHelperText';

const styles = theme => ({
  root: {
    marginTop: 25,
    display: 'flex',
  },
  formLabel: {
    marginBottom: 5,
    display: 'flex',
    float: 'left',
  },
  labelRadio: {
    height: 30,
    display: 'flex',
    float: 'left',
    margin: `${theme.spacing.unit * 6}px 15`,
  },
  groupRow: {
    flexDirection: 'row',
    float: 'left',
  },
});

export const RadioGroup = ({
  label,
  source,
  disabled,
  row,
  classes,
  // redux-form props
  input,
  meta: { touched, error },
}) => (
  <FormControl className={classes.root}>
    <FormLabel className={classes.formLabel}>{label}</FormLabel>
    <RadioButtonGroup
      // className={(row && classes.groupRow) || null}
      className={classes.groupRow}
      {...input}
      value={input.value + ''}
    >
      {source.map((el, i) => (
        <FormControlLabel
          key={i}
          className={classes.labelRadio}
          value={el.value}
          label={el.label}
          disabled={disabled}
          control={<Radio color="primary" />}
        />
      ))}
    </RadioButtonGroup>
    {touched && error && <FormHelperText error>{error}</FormHelperText>}
  </FormControl>
);

RadioGroup.displayName = 'RadioGroup';

RadioGroup.propTypes = {
  label: PropTypes.string,
  source: PropTypes.array.isRequired,
  disabled: PropTypes.bool,
  row: PropTypes.bool,
  classes: PropTypes.object,
  // redux-form props
  input: PropTypes.object,
};

export default withStyles(styles, { name: 'RadioGroup' })(RadioGroup);
