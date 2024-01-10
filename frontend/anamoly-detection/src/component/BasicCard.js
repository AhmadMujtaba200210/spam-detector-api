import * as React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import TextField from '@mui/material/TextField';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import { styled, keyframes } from '@mui/system';

const colorChange = keyframes`
  from {
    color: green;
  }

  to {
    color: red;
  }
`;

const Line = styled('div')`
  height: 3px;
  width: 70%;
  margin: 0 auto;
  background-color: ${({ color }) => color || 'green'};
  animation: ${colorChange} 1s ease-in-out;
`;

const SquareCardWithDetection = () => {
  const [inputText, setInputText] = React.useState('');
  const [apiResponse, setApiResponse] = React.useState(null);

  const handleInputChange = (event) => {
    setInputText(event.target.value);
    setApiResponse(null);
  };

  const handleApiSubmit = () => {
    const isHam = Math.random() < 0.5;
    setApiResponse(isHam ? 'ham' : 'spam');
  };

  return (
    <Box
      sx={{
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center',
        height: '100vh',
      }}
    >
      <Card sx={{ backgroundColor: 'black', color: 'white', width: '300px', height: '300px' }}>
        <CardContent sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
          <Typography variant="h6" sx={{ color: 'white', marginBottom: 2 }}>
            Spam or Ham Detection
          </Typography>
          <TextField
            label="Enter text"
            variant="outlined"
            fullWidth
            value={inputText}
            onChange={handleInputChange}
            sx={{
              marginBottom: 2,
              '& .MuiOutlinedInput-root': {
                '& fieldset': {
                  borderColor: 'white',
                },
                '&:hover fieldset': {
                  borderColor: 'white',
                },
                '&.Mui-focused fieldset': {
                  borderColor: 'white',
                },
              },
              '& .MuiInputLabel-root': {
                color: 'white',
              },
              '& .MuiInputBase-root': {
                color: 'white',
              },
            }}
          />
          <Button variant="contained" color="primary" onClick={handleApiSubmit}>
            Submit to API
          </Button>
        </CardContent>
        {apiResponse !== null && (
          <Line color={apiResponse === 'ham' ? 'green' : 'red'} />
        )}
      </Card>
    </Box>
  );
};

export default SquareCardWithDetection;
