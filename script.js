document.addEventListener("DOMContentLoaded", () => {
  const mobileMenuBtn = document.querySelector(".mobile-menu-btn");
  const mainNav = document.querySelector(".main-nav");

  if (mobileMenuBtn && mainNav) {
    mobileMenuBtn.addEventListener("click", () => {
      mainNav.classList.toggle("active");

      // Optional: toggle icon state if you want to animate it
      // mobileMenuBtn.classList.toggle('open');
    });
  }

  // Simple JavaScript to handle the toggle
  const accordions = document.querySelectorAll(".accordion-header");

  accordions.forEach((accordion) => {
    accordion.addEventListener("click", function () {
      // Toggle active class on header
      this.classList.toggle("active");

      // Handle the content height for animation
      const content = this.nextElementSibling;
      if (content.style.maxHeight) {
        content.style.maxHeight = null;
      } else {
        content.style.maxHeight = content.scrollHeight + "px";
      }
    });
  });
});
