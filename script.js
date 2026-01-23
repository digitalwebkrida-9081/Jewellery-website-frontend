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
});
