from flask import Flask, render_template, request, redirect, url_for
#from flask_socketio import SocketIO

app = Flask(__name__)
#socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template("index.html")

#@socketio.on('message')
#def handle_message(msg):
#    app.logger.info("{} se ha unido".format(msg['username']))

@app.route('/chat')
def chat():
    user = request.args.get('username')
    if user:
        return render_template("chat.html", username=user)
    else:
        return redirect(url_for('home'))

if __name__=='__main__':
    app.run(port=5000,debug=True)