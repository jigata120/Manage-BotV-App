
        // Daily Interactions Chart
        const interactionsCtx = document.getElementById('interactionsChart').getContext('2d');
        new Chart(interactionsCtx, {
            type: 'line',
            data: {
                labels: ['Feb 11', 'Feb 12', 'Feb 13', 'Feb 14', 'Feb 15'],
                datasets: [{
                    label: 'Daily Interactions',
                    data: [276, 289, 342, 315, 365],
                    borderColor: '#0F9DFF',
                    backgroundColor: 'rgba(15, 157, 255, 0.1)',
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { display: false }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: { color: '#A6A6A6' },
                        grid: { color: 'rgba(255,255,255,0.1)' }
                    },
                    x: {
                        ticks: { color: '#A6A6A6' },
                        grid: { display: false }
                    }
                }
            }
        });

        // Token Usage Distribution Chart
//<!--        const tokenUsageCtx = document.getElementById('tokenUsageChart').getContext('2d');-->
//<!--        new Chart(tokenUsageCtx, {-->
//<!--            type: 'pie',-->
//<!--            data: {-->
//<!--                labels: ['Daily Tokens', 'Monthly Tokens', 'Total Tokens'],-->
//<!--                datasets: [{-->
//<!--                    data: [24350, 532890, 1245670],-->
//<!--                    backgroundColor: ['#0F9DFF', '#7B61FF', '#38E45A']-->
//<!--                }]-->
//<!--            },-->
//<!--            options: {-->
//<!--                responsive: true,-->
//<!--                plugins: {-->
//<!--                    legend: {-->
//<!--                        position: 'bottom',-->
//<!--                        labels: { color: '#A6A6A6' }-->
//<!--                    }-->
//<!--                }-->
//<!--            }-->
//<!--        });-->

        // Activity Timeline Chart
        const activityTimelineCtx = document.getElementById('activityTimelineChart').getContext('2d');
        new Chart(activityTimelineCtx, {
            type: 'bar',
            data: {
                labels: ['Feb 11', 'Feb 12', 'Feb 13', 'Feb 14', 'Feb 15'],
                datasets: [{
                    label: 'Active Hours',
                    data: [18, 20, 22, 19, 21],
                    backgroundColor: '#0F9DFF'
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { display: false }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: { color: '#A6A6A6' },
                        grid: { color: 'rgba(255,255,255,0.1)' }
                    },
                    x: {
                        ticks: { color: '#A6A6A6' },
                        grid: { display: false }
                    }
                }
            }
        });
