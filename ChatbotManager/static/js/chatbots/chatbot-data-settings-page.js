    let contextEntries = [];
    let tokenCount = 0;

    document.addEventListener('DOMContentLoaded', () => {
        updateStats();
        setupEventListeners();
    });

    function updateStats() {
        document.getElementById('totalEntries').textContent = contextEntries.length;
        document.getElementById('tokenUsage').textContent = `${tokenCount}/500`;
        document.getElementById('lastUpdated').textContent = new Date().toLocaleString();
    }

    function setupEventListeners() {
        document.getElementById('newEntryForm').addEventListener('submit', (e) => {
            addNewEntry();
        });

        document.querySelector('.search-bar').addEventListener('input', (e) => {
            filterEntries(e.target.value);
        });

        document.getElementById('exportBtn').addEventListener('click', exportData);

        document.getElementById('clearBtn').addEventListener('click', clearAllData);
    }

    function addNewEntry() {
        const entryText = document.getElementById('entryText').value;
        const tags = document.getElementById('entryTags').value.split(',').map(tag => tag.trim());
        const isPriority = document.getElementById('isPriority').checked;
        const expirationDate = document.getElementById('expirationDate').value;

        const newEntry = {
            id: `entry-${Date.now()}`,
            text: entryText,
            tags: tags,
            isPriority: isPriority,
            expirationDate: expirationDate,
            timestamp: new Date().toISOString()
        };

        contextEntries.push(newEntry);
        updateStats();
        renderEntries();
        document.getElementById('newEntryForm').reset();

    }

    function renderEntries() {
        const tbody = document.getElementById('entriesTableBody');
        tbody.innerHTML = '';

        contextEntries.forEach(entry => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${entry.id}</td>
                <td>${entry.text.substring(0, 50)}${entry.text.length > 50 ? '...' : ''}</td>
                <td>${new Date(entry.timestamp).toLocaleString()}</td>
                <td>
                    <button class="btn btn-secondary" onclick="editEntry('${entry.id}')">Edit</button>
                    <button class="btn btn-danger" onclick="deleteEntry('${entry.id}')">Delete</button>
                </td>
            `;
            tbody.appendChild(row);
        });
    }

    function filterEntries(searchTerm) {
        const filteredEntries = contextEntries.filter(entry =>
            entry.text.toLowerCase().includes(searchTerm.toLowerCase()) ||
            entry.tags.some(tag => tag.toLowerCase().includes(searchTerm.toLowerCase()))
        );
        renderFilteredEntries(filteredEntries);
    }

    function renderFilteredEntries(entries) {
        const tbody = document.getElementById('entriesTableBody');
        tbody.innerHTML = '';

        entries.forEach(entry => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${entry.id}</td>
                <td>${entry.text.substring(0, 50)}${entry.text.length > 50 ? '...' : ''}</td>
                <td>${new Date(entry.timestamp).toLocaleString()}</td>
                <td>
                    <button class="btn btn-secondary" onclick="editEntry('${entry.id}')">Edit</button>
                    <button class="btn btn-danger" onclick="deleteEntry('${entry.id}')">Delete</button>
                </td>
            `;
            tbody.appendChild(row);
        });
    }

    function editEntry(id) {
        const entry = contextEntries.find(e => e.id === id);
        if (!entry) return;

        document.getElementById('entryText').value = entry.text;
        document.getElementById('entryTags').value = entry.tags.join(', ');
        document.getElementById('isPriority').checked = entry.isPriority;
        document.getElementById('expirationDate').value = entry.expirationDate;

        deleteEntry(id);

        document.querySelector('.add-entry-form').scrollIntoView({ behavior: 'smooth' });
    }

    function deleteEntry(id) {
        contextEntries = contextEntries.filter(entry => entry.id !== id);
        updateStats();
        renderEntries();
    }

    function exportData() {
        const dataStr = JSON.stringify(contextEntries, null, 2);
        const dataUri = 'data:application/json;charset=utf-8,'+ encodeURIComponent(dataStr);

        const exportFileDefaultName = 'context-data.json';

        const linkElement = document.createElement('a');
        linkElement.setAttribute('href', dataUri);
        linkElement.setAttribute('download', exportFileDefaultName);
        linkElement.click();
    }

    function clearAllData() {
        if (confirm('Are you sure you want to clear all context data? This action cannot be undone.')) {
            contextEntries = [];
            tokenCount = 0;
            updateStats();
            renderEntries();
        }
    }