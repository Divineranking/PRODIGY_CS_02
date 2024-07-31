document.addEventListener('DOMContentLoaded', () => {
    const passwordInput = document.getElementById('password');
    const strengthMeter = document.getElementById('strength-meter');
    const strengthText = document.getElementById('strength-text');

    function checkPasswordStrength(password) {
        let strength = 0;
        const lengthCriteria = password.length >= 8;
        const upperCaseCriteria = /[A-Z]/.test(password);
        const lowerCaseCriteria = /[a-z]/.test(password);
        const digitCriteria = /[0-9]/.test(password);
        const specialCharCriteria = /[!@#$%^&*(),.?":{}|<>]/.test(password);

        if (lengthCriteria) strength += 1;
        if (upperCaseCriteria) strength += 1;
        if (lowerCaseCriteria) strength += 1;
        if (digitCriteria) strength += 1;
        if (specialCharCriteria) strength += 1;

        return strength;
    }

    function updateStrengthMeter(strength) {
        let strengthColor;
        let strengthTextContent;

        switch (strength) {
            case 5:
                strengthColor = 'green';
                strengthTextContent = 'Password strength: Strong';
                break;
            case 4:
                strengthColor = 'yellowgreen';
                strengthTextContent = 'Password strength: Good';
                break;
            case 3:
                strengthColor = 'yellow';
                strengthTextContent = 'Password strength: Fair';
                break;
            case 2:
                strengthColor = 'orange';
                strengthTextContent = 'Password strength: Weak';
                break;
            default:
                strengthColor = 'red';
                strengthTextContent = 'Password strength: Very Weak';
                break;
        }

        strengthMeter.style.width = (strength * 20) + '%';
        strengthMeter.style.backgroundColor = strengthColor;
        strengthText.textContent = strengthTextContent;
    }

    passwordInput.addEventListener('input', () => {
        const password = passwordInput.value;
        const strength = checkPasswordStrength(password);
        updateStrengthMeter(strength);
    });
});
