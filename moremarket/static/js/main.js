// Page Transition Effect
document.addEventListener("DOMContentLoaded", function () {
    document.body.style.opacity = "1";
});

window.addEventListener("beforeunload", function () {
    document.body.style.opacity = "0";
});
// Scroll Reveal Effect
const cards = document.querySelectorAll(".card");

const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = 1;
            entry.target.style.transform = "translateY(0)";
        }
    });
});

cards.forEach(card => {
    card.style.opacity = 0;
    card.style.transform = "translateY(40px)";
    card.style.transition = "all 0.6s ease";
    observer.observe(card);
});
// ==============================
// LOCATION SYSTEM - FINAL CLEAN
// ==============================

function toggleLocationDropdown() {

    const dropdown = document.getElementById("locationDropdown");

    const isActive = dropdown.classList.contains("active");

    if (isActive) {
        closeLocationDropdown();
    } else {
        openLocationDropdown();
    }
}

// Close on outside click
document.addEventListener("click", function (e) {
    const wrapper = document.querySelector(".location-wrapper");
    if (!wrapper.contains(e.target)) {
        closeLocationDropdown();
    }
});

// ----------------------------
// GPS Detection
// ----------------------------

function detectLocation() {

    if (!navigator.geolocation) {
        alert("Geolocation not supported");
        return;
    }

    navigator.geolocation.getCurrentPosition(
        function (position) {

            const lat = position.coords.latitude;
            const lon = position.coords.longitude;

            fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lon}`)
                .then(res => res.json())
                .then(data => {

                    fillAddressFields(data.address);
                });

        },
        function () {
            alert("Location permission denied");
        }
    );
}

// ----------------------------
// Fetch from Pincode
// ----------------------------

function fetchFromPincode() {

    let pin = document.getElementById("manualPincode").value.trim();

    if (!/^[0-9]{6}$/.test(pin)) return;

    fetch(`https://api.postalpincode.in/pincode/${pin}`)
        .then(res => res.json())
        .then(data => {

            if (data[0].Status !== "Success") return;

            let postOffice = data[0].PostOffice[0];

            document.getElementById("manualCity").value = postOffice.District;
            document.getElementById("manualState").value = postOffice.State;

        });
}

// ----------------------------
// Fill Fields (GPS)
// ----------------------------

function fillAddressFields(address) {

    document.getElementById("manualArea").value =
        address.suburb ||
        address.neighbourhood ||
        address.village ||
        "";

    document.getElementById("manualCity").value =
        address.city ||
        address.town ||
        address.state ||
        "";

    document.getElementById("manualState").value =
        address.state || "";

    document.getElementById("manualPincode").value =
        address.postcode || "";
}

// ----------------------------
// Save Manual Address
// ----------------------------

function applyManualAddress() {

    let area = document.getElementById("manualArea").value.trim();
    let city = document.getElementById("manualCity").value.trim();
    let state = document.getElementById("manualState").value.trim();
    let pin = document.getElementById("manualPincode").value.trim();

    if (!pin) {
        alert("Pincode required");
        return;
    }

    let fullAddress = `${area}, ${city}, ${state} ${pin}`;

    // Short display version for navbar
    let shortDisplay = `${area}, ${city} ${pin}`;

    if (shortDisplay.length > 30) {
        shortDisplay = shortDisplay.substring(0, 30) + "...";
    }

document.getElementById("selected-location").innerText = shortDisplay;

    document.getElementById("selected-location").innerText = shortDisplay;

    localStorage.setItem("userFullAddress", fullAddress);
    localStorage.setItem("userLocation", shortDisplay);

    closeLocationDropdown();
}

// ----------------------------
// Load Saved
// ----------------------------

document.addEventListener("DOMContentLoaded", function () {

    let saved = localStorage.getItem("userLocation");

    if (saved) {
        document.getElementById("selected-location").innerText = saved;
    } else {
        document.getElementById("selected-location").innerText = "India (Any Area)";
    }

});

function selectSavedAddress(locationText) {
    document.getElementById("selected-location").innerText = locationText;

    fetch("/save-location/", {
        method: "POST",
        headers: {
            "X-CSRFToken": getCSRFToken(),
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: `location=${locationText}`
    });

    closeLocationDropdown();
    showToast();
}

function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}
document.addEventListener("click", function(event) {
    const dropdown = document.getElementById("locationDropdown");
    const wrapper = document.querySelector(".location-wrapper");

    if (!wrapper.contains(event.target)) {
        dropdown.classList.remove("active");
    }
});
// Auto move OTP input
function moveNext(input, index) {
    if (input.value.length === 1 && index < 6) {
        document.getElementsByClassName("otp-input")[index].focus();
    }
}

// 30 sec Timer
let timeLeft = 30;
let timer = document.getElementById("timer");
let resendBtn = document.getElementById("resendBtn");

if (timer) {
    let countdown = setInterval(() => {
        timeLeft--;
        timer.innerText = timeLeft;

        if (timeLeft <= 0) {
            clearInterval(countdown);
            resendBtn.disabled = false;
            timer.innerText = 0;
        }
    }, 1000);
}

// Fake loading verify animation
function verifyOTP() {
    let inputs = document.getElementsByClassName("otp-input");
    let otp = "";

    for (let i = 0; i < inputs.length; i++) {
        otp += inputs[i].value;
    }

    if (otp.length !== 6) {
        showMessage("Enter valid 6-digit OTP");
        return;
    }

    // Show loading effect
    let btn = document.querySelector(".auth-btn");
    btn.innerText = "Verifying...";
    btn.disabled = true;

    setTimeout(() => {
        btn.innerText = "Verify OTP";
        btn.disabled = false;

        // You can replace this with real AJAX
        showMessage("Invalid OTP (1/3)");

    }, 3000);
}

function showMessage(msg) {
    let box = document.getElementById("otpMessage");
    box.innerText = msg;
    box.style.display = "block";
}

// Resend OTP
function resendOTP() {
    resendBtn.disabled = true;
    timeLeft = 30;
}
function openLocationDropdown() {

    const dropdown = document.getElementById("locationDropdown");

    dropdown.classList.add("active");
    document.body.style.overflow = "hidden";  // Prevent background scroll

    // Auto detect only once when opening
    if (!dropdown.dataset.loaded) {
        detectLocation();
        dropdown.dataset.loaded = "true";
    }
}

function closeLocationDropdown() {

    const dropdown = document.getElementById("locationDropdown");

    dropdown.classList.remove("active");
    document.body.style.overflow = ""; // Restore scroll
}
document.addEventListener("click", function (e) {

    const dropdown = document.getElementById("locationDropdown");
    const trigger = document.querySelector(".location-trigger");

    if (
        dropdown.classList.contains("active") &&
        !dropdown.contains(e.target) &&
        !trigger.contains(e.target)
    ) {
        closeLocationDropdown();
    }

});
document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
        closeLocationDropdown();
    }
});
