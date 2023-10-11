const express = require('express');

const app = express()

app.get('/', (req, res) => {
  res.status(200).send('Homepage')
})

app.get('/about', () => {
  res.status(200).send('About Page')
})

app.all('*', () => {
  res.status(404).send('<h> Resource not Found </>')
}) 

app.listen(5000, () => {
  console.log('server is listening on port 5000');
});
