document.getElementById('playgroundBtn').addEventListener('click', () => {
            alert('Redirecting to Playground...');
        });

        document.getElementById('changePlanBtn').addEventListener('click', () => {
            alert('Opening plan selection...');
        });

        document.getElementById('backBtn').addEventListener('click', () => {
            alert('Going back to previous page...');
        });

        document.getElementById('purchaseBtn').addEventListener('click', () => {
            alert('Processing purchase...');
        });

        // Simple form validation
        const form = document.querySelector('.purchase-form');
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const card = document.getElementById('card').value;

            if (!name || !email || !card) {
                alert('Please fill in all required fields');
                return;
            }

            alert('Purchase successful! Thank you for your order.');
        });