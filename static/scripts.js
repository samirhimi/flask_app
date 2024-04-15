document.addEventListener('DOMContentLoaded', () => {
    fetch('/api/podinfo')
        .then(response => response.json())
        .then(data => {
            document.getElementById('hostname').textContent = `Hostname: ${data.hostname}`;
            document.getElementById('cpu-usage').textContent = `CPU Usage: ${data.cpu_usage}%`;
            document.getElementById('memory-usage').textContent = `Memory Usage: ${data.mem_usage}%`;
            document.getElementById('ip-address').textContent = `IP Address: ${data.ip}`;
        })
        .catch(error => console.error('Error:', error));
});
