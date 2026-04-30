const togglePassword = document.querySelector('#togglePassword');

togglePassword.addEventListener('click', function () {
    const passwordFields = document.querySelectorAll('input[type="password"], input[data-is-password="true"]');
    
    passwordFields.forEach(field => {
        const isPassword = field.getAttribute('type') === 'password';
        field.setAttribute('type', isPassword ? 'text' : 'password');
        field.setAttribute('data-is-password', 'true');
    });
});