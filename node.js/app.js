// simple server on Node.js


//require module http
const http = require('http')

// use localhost so use loopback address
const hostname = '127.0.0.1';

// set port
const port = 3000;

// start server
const server = http.createServer((req,res) => {

  // everything ok
  res.statusCode = 200;

  // set content-type header
  res.setHeader('Content-type','text/plain');
  res.end('Hello World!');
});

server.listen(port,hostname,() => {
  console.log('server started on port ' + port);
});
