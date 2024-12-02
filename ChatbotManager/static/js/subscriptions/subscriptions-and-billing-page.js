 document.addEventListener('DOMContentLoaded', function() {

        const months = ['May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'];


        const usageCtx = document.getElementById('usageChart').getContext('2d');
        new Chart(usageCtx, {
            type: 'line',
            data: {
                labels: months,
                datasets: [{
                    label: 'API Calls',
                    data: [3200, 3800, 3500, 4200, 3900, 4500],
                    borderColor: '#0F9DFF',
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        labels: {
                            color: '#E0E0E0'
                        }
                    }
                },
                scales: {
                    y: {
                        grid: {
                            color: '#162447'
                        },
                        ticks: {
                            color: '#A6A6A6'
                        }
                    },
                    x: {
                        grid: {
                            color: '#162447'
                        },
                        ticks: {
                            color: '#A6A6A6'
                        }
                    }
                }
            }
        });

        // Cost Chart
        const costCtx = document.getElementById('costChart').getContext('2d');
        new Chart(costCtx, {
            type: 'bar',
            data: {
                labels: months,
                datasets: [{
                    label: 'Monthly Cost ($)',
                    data: [99, 99, 99, 99, 99, 99],
                    backgroundColor: '#7B61FF',
                    borderRadius: 4
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        labels: {
                            color: '#E0E0E0'
                        }
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        grid: {
                            color: '#162447'
                        },
                        ticks: {
                            color: '#A6A6A6'
                        }
                    },
                    x: {
                        grid: {
                            color: '#162447'
                        },
                        ticks: {
                            color: '#A6A6A6'
                        }
                    }
                }
            }
        });
    });

    document.querySelector('.settings-form').addEventListener('submit', function(e) {
        e.preventDefault();
        const spendingCap = document.getElementById('spending-cap').value;
        const alertThreshold = document.getElementById('alert-threshold').value;

        console.log('Settings saved:', {
            spendingCap,
            alertThreshold
        });

        alert('Settings saved successfully!');
    });

    document.querySelectorAll('.btn-secondary').forEach(button => {
        if (button.textContent.includes('Switch')) {
            button.addEventListener('click', function() {
                const planName = this.textContent.replace('Switch to ', '');
                if (confirm(`Are you sure you want to switch to the ${planName} plan?`)) {
                    console.log(`Switching to ${planName} plan`);
                }
            });
        }
    });