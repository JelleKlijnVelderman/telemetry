// Maak de socket verbinding aan met de server
const socket = io();

// Maak een Chart.js grafiek
const ctx = document.getElementById('myChart').getContext('2d');
const telemetryChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Snelheid (km/u)',
            data: [],
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 2,
            fill: false
        }, {
            label: 'Temperatuur (°C)',
            data: [],
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 2,
            fill: false
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true,
                min: 0,
                max: 200,
            }
        }
    }
});

// Ontvang real-time data van de server via Socket.IO
socket.on('telemetry_update', function(msg) {
    console.log("Ontvangen data:", msg);

    // Parse de JSON-string om de gegevens te verkrijgen
    const data = JSON.parse(msg.data);  // Parse de geneste data

    console.log("Huidige snelheid:", data.snelheid, "Huidige temperatuur:", data.temperatuur);  // Log de individuele waarden

    telemetryChart.data.labels.push(new Date().toLocaleTimeString());
    telemetryChart.data.datasets[0].data.push(data.snelheid);  // Gebruik data.snelheid
    telemetryChart.data.datasets[1].data.push(data.temperatuur);  // Gebruik data.temperatuur

    // Verwijder oude data indien nodig
    if (telemetryChart.data.labels.length > 20) {
        telemetryChart.data.labels.shift();
        telemetryChart.data.datasets[0].data.shift();
        telemetryChart.data.datasets[1].data.shift();
    }

    telemetryChart.update();
});
