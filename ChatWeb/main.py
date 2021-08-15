from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, send
from win10toast import ToastNotifier
import joblib

app = Flask(__name__) # Crea la app
app.config['SECRET_KEY'] = 'mysecret' # Configura una contraseña
socketio = SocketIO(app, cors_allowed_origins="*") # Crea el socket
clf = joblib.load('../Classifier/GroomerClassifier.pkl') # Cargar el modelo clasificador
toast = ToastNotifier() # Instanciar el objeto para la alerta

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
    socketio.emit('typing', user, broadcast=True) # Evento para indicar que un usuarios esta escribiendo


@socketio.on('message')
def handle_message(data):
    socketio.emit('message', data) # Devuelve a todos los usuarios concetados el mensaje recivido
    msg_prob = clf.predict_proba([data['message']]) # Ingresa el mensaje al clasificador
    if msg_prob[0][1]*100 > 80: # Evalua para descartar falsos positivos
        toast.show_toast("Alerta", "Se ha detectado contenido Grooming en el chat!", duration=4) # Muestra la alerta    


if __name__=='__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True) # Ejecuta el servidor