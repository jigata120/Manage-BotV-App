    function showNotification(message, type = 'info') {
        const notification = document.createElement('div');
        notification.style.position = 'fixed';
        notification.style.top = '4rem';
        notification.style.right = '1rem';
        notification.style.padding = '1rem';
        notification.style.borderRadius = '8px';
        notification.style.backgroundColor = type === 'error' ? '#FF4F6D' : '#38E45A';
        notification.style.color = '#FFFFFF';
        notification.textContent = message;

        document.body.appendChild(notification);

        setTimeout(() => {
            notification.remove();
        }, 3000);
    }

    function showNewBotModal() {
        showNotification('New bot creation coming soon!');
    }

    document.querySelectorAll('.card').forEach(card => {
        card.addEventListener('mouseover', () => {
            card.style.transform = 'translateY(-5px)';
            card.style.boxShadow = '0 8px 12px rgba(0, 0, 0, 0.2)';
        });

        card.addEventListener('mouseout', () => {
            card.style.transform = 'translateY(0)';
            card.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)';
        });
    });

    document.querySelectorAll('.metric-value').forEach(metric => {
        const finalValue = parseInt(metric.textContent);
        let currentValue = 0;

        const interval = setInterval(() => {
            currentValue = Math.min(currentValue + Math.ceil(finalValue / 20), finalValue);
            metric.textContent = currentValue;

            if (currentValue === finalValue) {
                clearInterval(interval);
            }
        }, 50);
    });

