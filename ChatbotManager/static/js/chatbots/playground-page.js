    window.addEventListener('load', () => {
        setTimeout(() => {
            document.getElementById('loading-overlay').style.display = 'none';
        }, 500);
    });

    document.querySelectorAll('.quick-button').forEach(button => {
        button.addEventListener('click', () => {
            console.log('Quick access button clicked:', button.textContent);
        });
    });

    document.querySelector('.usage-progress').style.width = '90%';