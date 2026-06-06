const registerAgentHandlers = require('./agentHandler');

const onConnection = (io) => (socket) => {
  // Register handlers for different entities if needed
  registerAgentHandlers(io, socket);
};

module.exports = onConnection;
