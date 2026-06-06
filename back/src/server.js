const http = require('http');
const { Server } = require('socket.io');
const app = require('./app');
const onConnection = require('./sockets/index');

const PORT = 3001;

const server = http.createServer(app);

const io = new Server(server, {
  cors: {
    origin: "*", // Adjust this for production security
    methods: ["GET", "POST"]
  }
});

// Initialize socket handlers
io.on('connection', onConnection(io));

server.listen(PORT, () => {
  console.log(`Servidor rodando na porta ${PORT}`);
  console.log(`WebSocket pronto para conexões.`);
});
