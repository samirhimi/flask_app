from flask import Flask
import socket 

app = Flask(__name__)

@app.route('/')
def get_hostname():
    # Get the hostname of the pod
    hostname = socket.gethostname()
    return f"Hostname: {hostname}"
    # Get ip address
    ip_address = socket.gethostbyname(hostname)
    return f"IP Address: {ip_address}"
    # Get pod name
    pod_name = os.getenv("POD_NAME")
    return f"Pod Name: {pod_name}"
    # Get os version
    os_version = os.getenv("OS_VERSION")
    return f"OS Version: {os_version}"
    # Get cpu info
    cpu_info = os.getenv("CPU_INFO")
    return f"CPU Info: {cpu_info}"
    # Get mem info 
    mem_info = os.getenv("MEM_INFO")
    return f"Mem Info: {mem_info}"
    # Get disk info
    disk_info = os.getenv("DISK_INFO")
    return f"Disk Info: {disk_info}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
