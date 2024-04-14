from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')

def get_pod_info():
    # Get the hostname of the pod
    hostname = socket.gethostname()

    # Get the IP address of the pod
    pod_ip = socket.getaddrinfo(hostname)

    return f"Hostname: {hostname}\nPod IP Address: {pod_ip}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)