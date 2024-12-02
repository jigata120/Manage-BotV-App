document.addEventListener('DOMContentLoaded', function() {
            const collapsibles = document.querySelectorAll('.collapsible');

            collapsibles.forEach(button => {
                button.addEventListener('click', function() {
                    const content = this.closest('.section').querySelector('.collapsible-content');
                    content.classList.toggle('expanded');

                    this.textContent = content.classList.contains('expanded') ? 'Hide' : 'Toggle';
                });
            });

            const generalSettingsForm = document.getElementById('generalSettings');
            generalSettingsForm.addEventListener('submit', function(e) {

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

            const progressBars = document.querySelectorAll('.progress-bar');
            progressBars.forEach(bar => {
                const fill = bar.querySelector('.progress-fill');
                fill.style.width = '0%';

                setTimeout(() => {
                    fill.style.width = '75%';
                }, 500);
            });
        });