from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, send
#from GroomClasifier import Clasifier

app = Flask(__name__) # Crea la app
app.config['SECRET_KEY'] = 'mysecret' # Configura una contraseña
socketio = SocketIO(app, cors_allowed_origins="*") # Crea el socket

@app.route('/')
# Funcion para la ruta principal
def home():
    return render_template("index.html") # Devuelve la pagina de inicio


@app.route('/chat')
# Funcion para la ruta del chat
def chat():
    user = request.args.get('username') # Obtiene el nombre de usuario de la peticion
    if user:
        return render_template("chat.html", username=user) # Si el username no es vacio devuelve la pagina del chat
    else:
        return redirect(url_for('home')) # Si el username es vacio se mantiene en la pagina de inicio


@socketio.on('typing')
def handle_typing(user):
    socketio.emit('typing', user, broadcast=False)


@socketio.on('message')
def handle_message(data):
    socketio.emit('message', data) # Devuelve a todos los usuarios concetados el mensaje recivido
    #Clasifier(data) Groom : No Groom


if __name__=='__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True) # Ejecuta el servidor