const express = require('express');

const app = express()

app.get('/', (req, res) => {
  res.status(200).send('Homepage')
})

app.get('/About',() => {
  res.status(200).send('About Us')
})

app.listen(5000, (req, res) => {
  console.log('Listening to port 5000');
})
