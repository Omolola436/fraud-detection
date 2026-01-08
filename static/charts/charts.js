function initCharts() {
    const ctx = document.getElementById('mainChart');
    if (!ctx) return;

    new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['10:00', '10:15', '10:30', '10:45', '11:00', '11:15', '11:30'],
            datasets: [{
                label: 'Valid Transactions',
                data: [65, 59, 80, 81, 56, 55, 40],
                borderColor: '#1F2937',
                tension: 0.4,
                fill: false
            },
            {
                label: 'Fraud Attempts',
                data: [5, 2, 8, 12, 4, 3, 1],
                borderColor: '#F97316',
                tension: 0.4,
                fill: false
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom'
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    grid: {
                        display: false
                    }
                },
                x: {
                    grid: {
                        display: false
                    }
                }
            }
        }
    });
}
