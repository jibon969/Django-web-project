const button = document.querySelector('.Subscribe_button');

const email = document.querySelector('#sub_email');
const feedbackemail = document.querySelector('.key-error-email');

email.addEventListener('keyup', (e) => {
    const emailval = e.target.value;

    email.classList.remove("is-invalid");
    feedbackemail.style.display = "none";
    button.disabled = false;

    if (emailval.length > 0) {
        fetch('/subscribe_validation', {
            body: JSON.stringify({ emailid: emailval }), method: "POST",
        }).then(res => res.json()).then(data => {
            if (data.email_error) {
                email.classList.add("is-invalid");
                feedbackemail.style.display = "block";
                feedbackemail.innerHTML = `<small>${data.email_error}</small>`;
                button.disabled = true;
            }
        });
    }
});