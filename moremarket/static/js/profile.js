document.addEventListener("DOMContentLoaded", function () {

    const menuItems = document.querySelectorAll(".profile-menu li");
    const sections = document.querySelectorAll(".profile-section");

    menuItems.forEach(item => {
        item.addEventListener("click", function () {

            // remove active from all
            menuItems.forEach(i => i.classList.remove("active"));
            this.classList.add("active");

            const tab = this.getAttribute("data-tab");

            // hide all sections
            sections.forEach(section => {
                section.style.display = "none";
            });

            // show selected section
            const activeSection = document.getElementById(tab);
            if (activeSection) {
                activeSection.style.display = "block";
            }
        });
    });

});