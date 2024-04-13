from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route('/')
def get_pod_info():
    # Get the hostname of the pod
    hostname = socket.gethostname()

    # Get the IP address of the pod
    pod_ip = os.environ.get('POD_IP')

    return f"Hostname: {hostname}\nPod IP Address: {pod_ip}"

if __name__ == '__main__':
    # Get the pod IP address from environment variables
    pod_ip = os.getenv('POD_IP', 'Unknown')
    
    # Print the pod IP address for reference
    print(f"Pod IP Address: {pod_ip}")

    app.run(debug=True, host='0.0.0.0')
