import React from 'react';
import { connect } from 'react-redux';
// import PropTypes from 'prop-types';

// import Button from '@material-ui/core/Button';
// import CardActions from '@material-ui/core/CardActions';
import Chip from '@material-ui/core/Chip';
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

function MenteeCard(props) {
  const { classes } = props;
  if (!props.mentee.areas_of_guidance.length) {
    return <div />;
  }
  let areasOfGuidance = props.mentee.areas_of_guidance.map(area => {
    return (
      <li key={area}>
        <Chip label={area} className={classes.chip} variant="outlined" />
      </li>
    );
  });
  return (
    <Card>
      <CardContent>
        <Typography>{<ul>{areasOfGuidance}</ul>}</Typography>
      </CardContent>
    </Card>
  );
}

const mapStateToProps = state => ({
  mentee: state.profile.mentee,
});

export default withStyles(styles, { name: 'MenteeCard' })(connect(mapStateToProps)(MenteeCard));
