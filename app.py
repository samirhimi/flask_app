from flask import Flask
import socket 

app = Flask(__name__)

@app.route('/')
def get_hostname():
    # Get the hostname of the pod
    hostname = socket.gethostname()
    return f"Hostname: {hostname}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')