from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = '6hfhr6ujfjb6hvsc56hev52#'
socketio = SocketIO(app)

@app.route('/ppt', methods=['GET', 'POST'])
def sessions():
    return render_template('index.html')

@app.route('/control', methods=['GET', 'POST'])
def presenter():
    return render_template('index2.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, debug=False)