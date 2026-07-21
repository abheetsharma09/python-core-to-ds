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

    // ---- Edit Modal Trigger ----
    const editModal = document.getElementById('editModal');
    const editClose = document.getElementById('editModalClose');

    document.addEventListener('click', (e) => {
        if (e.target.closest('.btn-edit')) {
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
