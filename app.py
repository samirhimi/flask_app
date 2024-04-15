from flask import Flask, render_template, jsonify
import socket
import psutil
import os

app = Flask(__name__)

@app.route('/')

def index():

    # Get the hostname of the pod
    hostname = socket.gethostname()

    # Get the CPU usage of the pod
    try:
        cpu_usage = psutil.cpu_percent()
    except psutil.AccessDenied:
        cpu_usage = 0

    # Get the memory usage of the pod
    try:
        mem_usage = psutil.virtual_memory().percent
    except psutil.AccessDenied:
        mem_usage = 0

    # Get the IP address of the pod
    try:
        pod_ip = socket.gethostbyname(hostname)
    except socket.gaierror:
        pod_ip = "Unable to resolve IP address"

    return render_template('index.html', hostname= hostname, cpu_usage= cpu_usage, mem_usage= mem_usage, ip=pod_ip)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')