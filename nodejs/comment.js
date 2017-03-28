const http = require('http');
const cookie_reader = require('cookie');
const querystring = require('querystring');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer().listen(port);
const io = require('socket.io').listen(server);

const redis = require('redis');
const sub = redis.createClient();

//Subscribe to the Redis chat channel
sub.subscribe('chat');

//Configure socket.io to store cookie set by Django
io.use((socket, next) => {
  socket.handshake.cookie = cookie_reader.parse(socket.handshake.headers.cookie);
    if(socket.handshake.cookie['sessionid']) {
      next()
    }
    else {
      next(new Error("not valid token"));
      socket.disconnect();
    }
});

//Configure socket.io to store cookie set by Django
io.sockets.on('connection', (socket) => {
    console.log('connected: ', socket.id);

    //Grab message from Redis and send to client
    sub.on('message', (channel, message) => {
      socket.send(JSON.parse(message));
    });

    //Client is sending message through socket.io
    socket.on('send_message', (message) => {
        console.log(message);
        values = querystring.stringify({
            theme: message.theme,
            comment: message.text,
            sessionid: socket.handshake.cookie['sessionid'],
        });

        console.log(values);

        var options = {
            host: 'localhost',
            port: 8000,
            path: '/node_api',
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Content-Length': values.length
            }
        };

        //Send message to Django server
        var req = http.request(options, (res) => {
            console.log(`STATUS: ${res.statusCode}`);
            console.log(`HEADERS: ${JSON.stringify(res.headers)}`);
            res.setEncoding('utf8');
            res.on('data', (chunk) => {
                console.log(`BODY: ${chunk}`);
            });

            res.on('end', () => {
                console.log('No more data in response.');
            });
          });

          req.on('error', (e) => {
              console.log(`problem with request: ${e.message}`);
          });

          // write data to request body
          req.write(values);
          req.end();
    });
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
