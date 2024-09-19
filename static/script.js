// Maak de socket verbinding aan met de server
const socket = io();

// Maak een Chart.js grafiek
const ctx = document.getElementById('telemetryChart').getContext('2d');
const telemetryChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [],  // Labels worden dynamisch toegevoegd
        datasets: [
            {
                label: 'Snelheid (km/u)',
                borderColor: 'rgb(255, 99, 132)',
                data: [],  // Data wordt dynamisch toegevoegd
                fill: false,
            },
            {
                label: 'Temperatuur (°C)',
                borderColor: 'rgb(54, 162, 235)',
                data: [],  // Data wordt dynamisch toegevoegd
                fill: false,
            }
        ]
    },
    options: {
        scales: {
            x: {
                title: {
                    display: true,
                    text: 'Tijd (samples)'
                }
            },
            y: {
                title: {
                    display: true,
                    text: 'Waarde'
                }
            }
        }
    }
});

// Luister naar updates van telemetriegegevens
socket.on('telemetry_update', function(msg) {
    console.log(msg.data);

    // Ontvang de sensorgegevens en splits deze in snelheid en temperatuur
    const sensorData = msg.data.split(', ');
    const snelheid = sensorData[0].split(': ')[1].split(' ')[0];
    const temperatuur = sensorData[1].split(': ')[1].split(' ')[0];

    // Voeg nieuwe data toe aan de grafiek
    telemetryChart.data.labels.push('');
    telemetryChart.data.datasets[0].data.push(snelheid);  // Snelheid dataset
    telemetryChart.data.datasets[1].data.push(temperatuur);  // Temperatuur dataset

    // Verwijder oude data om de grafiek overzichtelijk te houden (max 50 punten)
    if (telemetryChart.data.labels.length > 50) {
        telemetryChart.data.labels.shift();
        telemetryChart.data.datasets[0].data.shift();
        telemetryChart.data.datasets[1].data.shift();
    }

    telemetryChart.update();
});
