document.addEventListener("DOMContentLoaded", () => {

    const cards = document.querySelectorAll(".program-card");

    cards.forEach((card) => {

        card.addEventListener("mouseenter", () => {
            card.style.cursor = "pointer";
        });

    });


    /*
        Smooth scrolling for links such as:

        Home
        Programs
        Faculty
    */

    document.querySelectorAll('a[href^="#"]').forEach((link) => {

        link.addEventListener("click", (event) => {

            const targetId =
                link.getAttribute("href");

            if (!targetId || targetId === "#") {
                return;
            }

            const target =
                document.querySelector(targetId);

            if (target) {

                event.preventDefault();

                target.scrollIntoView({
                    behavior: "smooth"
                });

            }

        });

    });

});