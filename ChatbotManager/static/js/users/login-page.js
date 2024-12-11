document.addEventListener('DOMContentLoaded', function() {
            const form = document.getElementById('signin-form');
            const googleButton = document.getElementById('google-signin');

            // Form validation
            form.addEventListener('submit', function(e) {
                e.preventDefault();

                // Reset errors
                clearErrors();

                let isValid = true;
                const email = document.getElementById('email').value;
                const password = document.getElementById('password').value;

                // Email validation
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (!emailRegex.test(email)) {
                    showError('email', 'Please enter a valid email address');
                    isValid = false;
                }

                // Password validation
                if (password.length < 1) {
                    showError('password', 'Please enter your password');
                    isValid = false;
                }

                if (isValid) {
                    // Show success message
                    document.getElementById('success-message').style.display = 'block';
                    form.reset();

                    // Hide success message after 3 seconds
                    setTimeout(() => {
                        document.getElementById('success-message').style.display = 'none';
                    }, 3000);
                }
            });

            // Google sign-in handler
            googleButton.addEventListener('click', function() {
                // In a real implementation, this would initialize the Google Sign-In flow
                alert('Google Sign-In would be initialized here');
            });

            // Helper functions
            function showError(field, message) {
                const errorElement = document.getElementById(`${field}-error`);
                errorElement.textContent = message;
                errorElement.style.display = 'block';
                document.getElementById(field).classList.add('error');
            }

            function clearErrors() {
                const errors = document.getElementsByClassName('error');
                for (let error of errors) {
                    error.style.display = 'none';
                }
            }
        });