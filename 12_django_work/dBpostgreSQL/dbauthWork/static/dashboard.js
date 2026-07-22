// script.js
document.addEventListener('DOMContentLoaded', () => {

    // ---- Dark Mode Toggle ----
    const darkToggle = document.getElementById('darkToggle');
    darkToggle.addEventListener('click', () => {
        document.body.classList.toggle('dark');
        const icon = darkToggle.querySelector('.toggle-icon');
        icon.textContent = document.body.classList.contains('dark') ? '☀️' : '🌙';
    });

    // ---- Add Modal Trigger ----
    const addBtn = document.getElementById('addNoteBtn');
    const addModal = document.getElementById('addModal');
    const addClose = document.getElementById('addModalClose');

    addBtn.addEventListener('click', () => addModal.classList.add('active'));
    addClose.addEventListener('click', () => addModal.classList.remove('active'));
    addModal.addEventListener('click', (e) => {
        if (e.target === addModal) addModal.classList.remove('active');
    });

    // ---- Edit Modal Trigger (FIXED FOR BACKEND DYNAMICS) ----
    const editModal = document.getElementById('editModal');
    const editClose = document.getElementById('editModalClose');
    const editForm = document.getElementById('editForm');
    const editTitleInput = editForm.querySelector('input[name="edit_title"]');
    const editDescInput = editForm.querySelector('textarea[name="edit_desc"]');

    document.addEventListener('click', (e) => {
        const editBtn = e.target.closest('.btn-edit');
        if (editBtn) {
            // 1. Get the dynamic note ID from your data-id attribute
            const noteId = editBtn.getAttribute('data-id');

            // 2. Find the note card wrapping this button
            const noteCard = editBtn.closest('.note-card');
            
            // 3. Extract the active text strings directly from the card
            const currentTitle = noteCard.querySelector('h3').textContent.trim();
            const currentDesc = noteCard.querySelector('p').textContent.trim();

            // 4. Populate your modal form fields with the current text data
            editTitleInput.value = currentTitle;
            editDescInput.value = currentDesc;

            // 5. Explicitly inject the correct route path into your form action
            editForm.method = 'POST';
            editForm.action = `/edit/${noteId}/`;

            // 6. Open the edit modal popup
            editModal.classList.add('active');
        }
    });

    editClose.addEventListener('click', () => editModal.classList.remove('active'));
    editModal.addEventListener('click', (e) => {
        if (e.target === editModal) editModal.classList.remove('active');
    });

    // ---- Close modals with Escape ----
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            if (addModal.classList.contains('active')) addModal.classList.remove('active');
            if (editModal.classList.contains('active')) editModal.classList.remove('active');
        }
    });

    // ---- Delete buttons show a dummy alert ----
    document.addEventListener('click', (e) => {
        if (e.target.closest('.btn-delete')) {
            alert('🗑️ Dummy delete – no data is actually removed.');
        }
    });
});
