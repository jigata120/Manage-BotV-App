document.addEventListener('DOMContentLoaded', function() {
            // Handle collapsible sections
            const collapsibles = document.querySelectorAll('.collapsible');

            collapsibles.forEach(button => {
                button.addEventListener('click', function() {
                    const content = this.closest('.section').querySelector('.collapsible-content');
                    content.classList.toggle('expanded');

                    // Update button text
                    this.textContent = content.classList.contains('expanded') ? 'Hide' : 'Toggle';
                });
            });

            // Handle form submission
            const generalSettingsForm = document.getElementById('generalSettings');
            generalSettingsForm.addEventListener('submit', function(e) {
                e.preventDefault();

                // Simulate saving changes
                const saveBtn = this.querySelector('button[type="submit"]');
                const originalText = saveBtn.textContent;

                saveBtn.textContent = 'Saving...';
                saveBtn.disabled = true;

                setTimeout(() => {
                    saveBtn.textContent = 'Saved!';
                    setTimeout(() => {
                        saveBtn.textContent = originalText;
                        saveBtn.disabled = false;
                    }, 1500);
                }, 1000);
            });

            // Initialize progress bar animation
            const progressBars = document.querySelectorAll('.progress-bar');
            progressBars.forEach(bar => {
                const fill = bar.querySelector('.progress-fill');
                fill.style.width = '0%';

                setTimeout(() => {
                    fill.style.width = '75%';
                }, 500);
            });
        });