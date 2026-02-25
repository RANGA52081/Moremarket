// Toggle password visibility
function togglePassword() {
    const input = document.getElementById("passwordInput");
    const icon = document.querySelector(".toggle-password");

    if (input.type === "password") {
        input.type = "text";
        icon.classList.remove("bi-eye-slash");
        icon.classList.add("bi-eye");
    } else {
        input.type = "password";
        icon.classList.remove("bi-eye");
        icon.classList.add("bi-eye-slash");
    }
}

// Shake on error
document.addEventListener("DOMContentLoaded", function () {
    const error = document.querySelector(".error-message");
    if (error) {
        document.getElementById("authCard").classList.add("shake");
    }
});
