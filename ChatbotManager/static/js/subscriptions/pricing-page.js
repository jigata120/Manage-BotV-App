 document.querySelectorAll('.faq-item').forEach(item => {
        item.addEventListener('click', () => {
            const wasActive = item.classList.contains('active');

            // Close all FAQ items
            document.querySelectorAll('.faq-item').forEach(faqItem => {
                faqItem.classList.remove('active');
            });

            // Toggle the clicked item if it wasn't already active
            if (!wasActive) {
                item.classList.add('active');
            }
        });
    });

    // Smooth scroll for navigation
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Add hover effect to price cards
    document.querySelectorAll('.price-card').forEach(card => {
        card.addEventListener('mouseover', () => {
            card.style.transform = 'translateY(-10px)';
        });

        card.addEventListener('mouseout', () => {
            card.style.transform = 'translateY(0)';
        });
    });