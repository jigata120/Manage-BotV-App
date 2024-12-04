 document.addEventListener('DOMContentLoaded', function() {
            const form = document.getElementById('signup-form');
            const googleButton = document.getElementById('google-signup');

            // Form validation
            form.addEventListener('submit', function(e) {
                e.preventDefault();

                // Reset errors
                clearErrors();

                let isValid = true;
                const username = document.getElementById('username').value;
                const email = document.getElementById('email').value;
                const password = document.getElementById('password').value;

                // Username validation
                if (username.length < 3) {
                    showError('username', 'Username must be at least 3 characters long');
                    isValid = false;
                }

                // Email validation
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (!emailRegex.test(email)) {
                    showError('email', 'Please enter a valid email address');
                    isValid = false;
                }

                // Password validation
                if (password.length < 8) {
                    showError('password', 'Password must be at least 8 characters long');
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

            // Google sign-up handler
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