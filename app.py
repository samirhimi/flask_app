from flask import Flask, render_template, jsonify
import socket

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/podinfo')
def get_pod_info():
    # Get the hostname of the pod
    hostname = socket.gethostname()

    # Get the IP address of the pod
    try:
        pod_ip = socket.gethostbyname(hostname)
    except socket.gaierror:
        pod_ip = "Unable to resolve IP address"

    return jsonify(hostname=hostname, ip=pod_ip)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
