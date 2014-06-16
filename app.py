from flask import Flask
from flask.ext.socketio import SocketIO, emit

app = Flask(__name__)
app.debug = True
socketio = SocketIO(app)

@app.route('/')
def hello_world():			 
	return 'Hello World!'

@socketio.on('connect', namespace='/test')
def test_connect():
	print "sending stuff"
	emit('stuff', {'data': 'Connected'})


@socketio.on('incoming_phone', namespace='/test')
def send_incoming(message):
	print "incoming phone called with message : " + str(message)
	emit("incoming", {'data': message})

if __name__ == '__main__':
    socketio.run(app)