import React from 'react';
import { connect } from 'react-redux';
// import PropTypes from 'prop-types';

// import Button from '@material-ui/core/Button';
// import CardActions from '@material-ui/core/CardActions';
import { withStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';

const styles = {
  card: {
    minWidth: 275,
  },
  bullet: {
    display: 'inline-block',
    margin: '0 2px',
    transform: 'scale(0.8)',
  },
  title: {
    marginBottom: 16,
    fontSize: 14,
  },
  pos: {
    marginBottom: 12,
  },
};

function AboutCard(props) {
  return (
    <Card>
      <CardContent>
        <Typography>{props.profile.bio}</Typography>
      </CardContent>
    </Card>
  );
}

const mapStateToProps = state => ({
  profile: state.profile.profile,
});

export default withStyles(styles, { name: 'AboutCard' })(connect(mapStateToProps)(AboutCard));
