const registerAgentHandlers = (io, socket) => {
  console.log(`Agente conectado: ${socket.id}`);
  socket.on('agent:init', (data) => {
    console.log(`novo PC conectado:`, data.pcName)
  })
  // Event to receive data from the agent
  socket.on('agent:data', (data) => {
    const obj = JSON.parse(data) 
    console.log(`[${socket.id} | ${obj.pcName}] dados: `, obj);
    
    // Here you can add logic to save to a database or forward to a frontend
    // socket.broadcast.emit('frontend:data', data);
  });

  socket.on('disconnect', (reason) => {
    console.log(`Agente desconectado: [${socket.name}] (${reason})`);
  });
};

module.exports = registerAgentHandlers;
