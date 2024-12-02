
        // Image upload handling
        const imageUpload = document.getElementById('imageUpload');
        const imagePreview = document.getElementById('imagePreview');
        const uploadText = document.getElementById('uploadText');

        ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
            imageUpload.addEventListener(eventName, preventDefaults, false);
        });

        function preventDefaults(e) {
            e.preventDefault();
            e.stopPropagation();
        }

        ['dragenter', 'dragover'].forEach(eventName => {
            imageUpload.addEventListener(eventName, highlight, false);
        });

        ['dragleave', 'drop'].forEach(eventName => {
            imageUpload.addEventListener(eventName, unhighlight, false);
        });

        function highlight(e) {
            imageUpload.classList.add('dragover');
        }

        function unhighlight(e) {
            imageUpload.classList.remove('dragover');
        }

        imageUpload.addEventListener('drop', handleDrop, false);
        imageUpload.addEventListener('click', () => {
            const input = document.createElement('input');
            input.type = 'file';
            input.accept = 'image/*';
            input.onchange = (e) => {
                const file = e.target.files[0];
                handleFile(file);
            };
            input.click();
        });

        function handleDrop(e) {
            const dt = e.dataTransfer;
            const file = dt.files[0];
            handleFile(file);
        }

        function handleFile(file) {
            if (file && file.type.startsWith('image/')) {
                const reader = new FileReader();
                reader.onload = (e) => {
                    imagePreview.querySelector('img').src = e.target.result;
                    imagePreview.style.display = 'block';
                    uploadText.style.display = 'none';
                };
                reader.readAsDataURL(file);
            }
        }

        // API Key copy functionality
        function copyApiKey() {
            const apiKey = document.getElementById('apiKey');
            navigator.clipboard.writeText(apiKey.textContent)
                .then(() => {
                    const btn = document.querySelector('.copy-btn');
                    btn.textContent = 'Copied!';
                    setTimeout(() => {
                        btn.textContent = 'Copy API Key';
                    }, 2000);
                });
        }
