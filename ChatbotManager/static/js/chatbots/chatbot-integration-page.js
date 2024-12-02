document.addEventListener('DOMContentLoaded', () => {
    const codeTabs = document.querySelectorAll('.code-tabs .tab');
    const codeBlocks = document.querySelectorAll('.code-block');

    codeTabs.forEach(tab => {
        tab.addEventListener('click', () => {
            codeTabs.forEach(t => t.classList.remove('active'));
            codeBlocks.forEach(block => block.classList.remove('active'));

            const lang = tab.dataset.lang;
            tab.classList.add('active');
            document.querySelector(`.code-block[data-lang="${lang}"]`).classList.add('active');
        });
    });

    const copyButtons = document.querySelectorAll('.copy-btn');
    copyButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const targetId = btn.dataset.clipboardTarget;
            const textToCopy = document.querySelector(targetId).textContent;

            navigator.clipboard.writeText(textToCopy).then(() => {
                btn.classList.add('copied');
                setTimeout(() => btn.classList.remove('copied'), 2000);
            }).catch(err => {
                console.error('Copy failed:', err);
            });
        });
    });

    const manageBtns = document.querySelectorAll('.manage-btn');
    manageBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const chatbotId = btn.closest('.chatbot-card').dataset.botId;
            console.log(`Manage Chatbot: ${chatbotId}`);
        });
    });
});
console.log('Modal or Delete button not found!');