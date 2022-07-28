from flask import Flask
from flask_socketio import SocketIO, emit


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)

@socketio.on('connect')
def connect():
    print("client connected")

@socketio.on('disconnect')
def disconnect():
    print('client disconnected')

@socketio.on('question')
def handle_questio(msg):
    print('question msg:', msg)
    socketio.emit("answer", "msg from server")

@socketio.on('help')
def handle_help(msg):
    print('help msg:', msg)
    socketio.emit("support", "help from server")
    
@app.route('/')
def hello():
    return "hii"

if __name__ == '__main__':
    print('start')
    socketio.run(app, host='0.0.0.0',port = 1212)
