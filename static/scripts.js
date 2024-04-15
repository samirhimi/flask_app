document.addEventListener('DOMContentLoaded', () => {
    fetch('/api/podinfo')
        .then(response => response.json())
        .then(data => {
            document.getElementById('hostname').textContent = `Hostname: ${data.hostname}`;
            document.getElementById('OS-version').textContent = `OS version: ${data.os_version}`;
            document.getElementById('CPU-Number').textContent = `CPU Number: ${data.num_cpus}`;
            document.getElementById('cpu-usage').textContent = `CPU Usage: ${data.cpu_usage}%`;
            document.getElementById('memory-usage').textContent = `Memory Usage: ${data.memory_usage} bytes`;
            document.getElementById('ip-address').textContent = `IP Address: ${data.ip}`;
        })
        .catch(error => console.error('Error:', error));
});
