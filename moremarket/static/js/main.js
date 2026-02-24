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

// Toggle dropdown
function toggleLocationDropdown() {
    document.getElementById("locationDropdown").classList.toggle("active");
}

function closeLocationDropdown() {
    document.getElementById("locationDropdown").classList.remove("active");
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