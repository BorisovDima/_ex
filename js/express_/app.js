var express = require('express');

var test_route = require('./routes/test_route.js')
var app = express();

app.use('/', test_route)

app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});
