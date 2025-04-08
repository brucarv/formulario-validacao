const form = document.getElementById('form');
const message = document.getElementById('message');

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value.trim();

    const response = await fetch('/validate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, email, password })
    });

    const result = await response.json();

    if (response.ok) {
        message.textContent = result.message;
        message.style.color = 'green';
    } else {
        message.innerHTML = result.errors.join('<br>');
        message.style.color = 'red';
    }
});
