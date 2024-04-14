document.addEventListener('DOMContentLoaded', () => {
    fetch('/api/podinfo')
        .then(response => response.json())
        .then(data => {
            document.getElementById('hostname').textContent = `Hostname: ${data.hostname}`;
            document.getElementById('ip-address').textContent = `IP Address: ${data.ip}`;
        })
        .catch(error => console.error('Error:', error));
});
