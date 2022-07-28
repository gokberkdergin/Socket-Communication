import socketio

sio = socketio.Client()

@sio.on('connect')
def connect():
    print('connected')

@sio.on('disconnect')
def disconnect():
    print('disconnected')

@sio.on('answer')
def answer(data):
    print('answer:', data)

@sio.on('support')
def support(data):
    print('support:', data)
    
# --- main ---

print('start')
sio.connect('http://localhost:1212')

print('sleep')
sio.sleep(1)

print('emit question')
sio.emit('question', {'foo': 'bar'})

print('emit help')
sio.emit('help', 'can you help me')

print('sleep')
sio.sleep(1)

sio.disconnect()
