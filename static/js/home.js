document.addEventListener("DOMContentLoaded", function() {
    const sections = document.querySelectorAll(".project-section");

    document.addEventListener("wheel", function(event) {
        event.preventDefault();

        const delta = Math.sign(event.deltaY);

        if (delta > 0) {
            scrollToNextSection();
        } else {
            scrollToPrevSection();
        }
    });

    let currentSectionIndex = 0;

    function scrollToNextSection() {
        if (currentSectionIndex < sections.length - 1) {
            currentSectionIndex++;
            sections[currentSectionIndex].scrollIntoView({ behavior: "smooth" });
        }
    }

    function scrollToPrevSection() {
        if (currentSectionIndex > 0) {
            currentSectionIndex--;
            sections[currentSectionIndex].scrollIntoView({ behavior: "smooth" });
        }
    }
});
