function closeModal() {
            document.getElementById('resultModal').classList.remove('active');
            // Optional: Remove the modal from DOM after animation
            setTimeout(() => {
                document.getElementById('resultModal').remove();
            }, 300);
        }

        // Close modal when clicking outside
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('modal-overlay')) {
                closeModal();
            }
        });

        // Close with Escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && document.getElementById('resultModal')) {
                closeModal();
            }
        });