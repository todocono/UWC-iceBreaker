let express = require('express');
let socket = require('socket.io');

//Express becomes accessible through app
let app = express();
//Create a server on localhost:5000
let server = app.listen(5000);
//Host content as static on public
app.use(express.static('public'));

console.log("Node is running on port 5000...");

//Allow server to use the socket
let io = socket(server);
//Dealing with server events / connection
//...when a new connection is on, run the newConnection function
io.sockets.on('connection', newConnection); //callback

//Function that serves the new connection
function newConnection(socket){
	console.log('New connection: ' + socket.id);

	//When a message arrives from the client, run the eventMessage function
	socket.on('eventFromClient', eventMessage);

	function eventMessage(dato){
		socket.broadcast.emit('eventFromServer', dato);
		//Following line refers to sending data to all clients
		//io.sockets.emit('mouse', data);
		//console.log(data);
	}
}


console.log("Hello, connecting to microbit");

const SerialPort = require('serialport')
const Readline = SerialPort.parsers.Readline;
const port = new SerialPort('/dev/tty.usbmodem141202', {
  baudRate: 115200,
  autoOpen: false,
  flowControl: false
})


const parser = port.pipe(new Readline({ delimiter: '\n' }));

let bitsArray = []
parser.on('data', function(data) {
   var bits = data;
   bitsArray.push(bits)
//   console.log(bits);
   processData(data);
 });


port.open(() => {
    console.log("Port open");
    parser.on('data', function(dataFromMicro) {

		//socket.broadcast.emit('eventFromMicrobit', data);
	   // processData(dataFromMicro);
		//showData(data)

		//When a message arrives from the client, run the eventMessage function
		//socket.on('eventFromClient', eventMessage);

		//function showData(data){
			//socket.broadcast.emit('eventFromMicroBit', data);
			//Following line refers to sending data to all clients
			//io.sockets.emit('mouse', data);
			//console.log(data);
		//}
    });
})


function processData(dataFromMicro) {
	io.emit('dataFromMicrobit', dataFromMicro );
    // bitsArray.forEach((bit) => {
    //     console.log(bit) //plot one by one here
    // })
  }
