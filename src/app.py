# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, jsonify
import datetime
import socket

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

@app.route('/api/v1/details')

def details():
    return jsonify({
        'time': datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y"),
        'hostname': socket.gethostname(),
        'message': 'You are doing great, human!'
    })

@app.route('/api/v1/healthz')
# ‘/’ URL is bound with hello_world() function.
def health():
    return jsonify({'status': 'up'}), 200

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host="0.0.0.0")



# '/api/v1/details'
# '/api/v1/healthz'