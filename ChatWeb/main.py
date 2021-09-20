from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO
from win10toast import ToastNotifier
import joblib, time

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
    if data['message']:
        socketio.emit('message', data) # Devuelve a todos los usuarios concetados el mensaje recivido
        msg_prob = clf.predict_proba([data['message']]) # Ingresa el mensaje al clasificador
        if msg_prob[0][1]*100 > 80: # Evalua para descartar falsos positivos
            toast.show_toast("Alerta", "Se ha detectado contenido Grooming en el chat!", icon_path='D:/IDE/Anaconda/envs/ProjectNLP/Software/ChatWeb/static/alert.ico', duration=4) # Muestra la alerta
            #toast.show_toast("Alerta", f"Se ha detectado contenido Grooming en el chat! \n Usuario: {data['user']} \n Registro de hora: {time.strftime('%H:%M:%S')}", icon_path='/static/alert.ico', duration=4) # Muestra la alerta
            #print("Usuario: ", data['user'])
            #print("Registro de hora: ", time.strftime('%H:%M:%S'))


if __name__=='__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True) # Ejecuta el servidor