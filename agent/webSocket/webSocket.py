import socketio
import time

import json

from data.CreateJsonData import checkIfJsonExists
from data.getData import getDataForTeacher


# Cria o cliente Socket.io
sio = socketio.Client()

jsonData = checkIfJsonExists()


@sio.event
def connect():
    print("Conectado ao servidor!")
    sio.emit('agent:init', {'pcName': jsonData["pcName"]})
    while True:
        
        # Assim que conectar, envia um dado de teste
        sio.emit('agent:data', json.dumps(getDataForTeacher(), default=str))
        time.sleep(5)

@sio.event
def disconnect():
    print("Desconectado do servidor.")
   
@sio.on('message') # Caso o servidor envie algo
def on_message(data):
    print('Mensagem recebida:', data)
   
   
if __name__ == '__main__':
    try:
        # Conecta ao endereço do servidor Node.js
        sio.connect('http://localhost:3001')
            
        # Mantém o script rodando
        sio.wait()
    except Exception as e:
        print(f"Erro ao conectar: {e}")
