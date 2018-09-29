import MenuItem from '@material-ui/core/MenuItem';
import MuiTextField from '@material-ui/core/TextField';
import PropTypes from 'prop-types';
import React from 'react';

// SelectField will show 5.5 menu items by default. Scrollbar will auto-show
// if there are more items.
const VISIBLE_MENU_ITEM_COUNT = 5.5;

// Hardcoded values from material-ui source
const MUI_MENU_ITEM_HEIGHT = 32;
const MUI_MENU_PADDING_TOP = 8;

const maxHeight = MUI_MENU_ITEM_HEIGHT * VISIBLE_MENU_ITEM_COUNT + MUI_MENU_PADDING_TOP;
const MenuProps = { PaperProps: { style: { maxHeight } } };

const SelectField = ({
  className,
  disabled,
  helperText,
  items,
  label,
  multiple,
  required,
  displayEmpty,
  input: { name, value, onBlur, onChange },
  meta: { touched, error } = {},
}) => {
  const hasError = touched && !!error;
  const hasHelperText = !!helperText;
  const separator = (hasError && hasHelperText && ' | ') || '';
  const combinedHelperText = (
    <span>
      {hasError && error}
      {separator}
      {hasHelperText && helperText}
    </span>
  );

  return (
    <MuiTextField
      select
      id={name}
      value={value || []}
      label={label}
      className={className}
      disabled={disabled}
      error={hasError}
      fullWidth
      margin="normal"
      required={required}
      helperText={combinedHelperText}
      SelectProps={{ MenuProps, multiple, displayEmpty }}
      onBlur={event => onBlur && onBlur(event.target.value)}
      onChange={event => onChange(event.target.value)}
    >
      {items &&
        items.map(item => (
          <MenuItem key={item.value} value={item.value}>
            {item.label}
          </MenuItem>
        ))}
    </MuiTextField>
  );
};

SelectField.propTypes = {
  input: PropTypes.shape({
    value: PropTypes.oneOfType([
      PropTypes.string,
      PropTypes.number,
      PropTypes.arrayOf(PropTypes.oneOfType([PropTypes.string, PropTypes.number])),
    ]),
    onChange: PropTypes.func.isRequired,
  }).isRequired,
  items: PropTypes.arrayOf(
    PropTypes.shape({
      value: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
      label: PropTypes.string,
    })
  ).isRequired,
};

SelectField.displayName = 'SelectField';

export default SelectField;
