function showNewBotModal() {
        document.getElementById('newBotModal').style.display = 'flex';
    }

    function showEditModal(botId) {
        document.getElementById('editBotModal').style.display = 'flex';
    }

    function showDeleteModal(botId) {
        document.getElementById('deleteBotModal').style.display = 'flex';
    }

    function closeModal(modalId) {
        document.getElementById(modalId).style.display = 'none';
    }