import { createMuiTheme } from '@material-ui/core/styles';

export default createMuiTheme({
  palette: {
    primary: {
      main: '#3f60fb',
    },
    secondary: {
      main: '#f6695d',
    },
  },
  overrides: {
    MuiButton: {
      root: {
        borderRadius: '30px',
      },
      raisedSecondary: {
        backgroundColor: '#FFFFFF',
        border: 'solid 1px #000000',
        '&:hover': {
          backgroundColor: '#D3D3D3',
        },
      },
    },
  },
});
