window.addEventListener("load", function () {
  if (window.innerWidth <= 991) {
    document.querySelector("nav").classList.add("mobile");
    document.querySelector(".nav-btn").classList.add("visible");
  } else {
    document.querySelector("nav").classList.remove("mobile");
    document.querySelector(".nav-btn").classList.remove("visible");
  }
});

window.addEventListener("resize", function () {
  if (window.innerWidth <= 991) {
    document.querySelector("nav").classList.add("mobile");
    document.querySelector(".nav-btn").classList.add("visible");
  } else {
    document.querySelector("nav").classList.remove("mobile");
    document.querySelector(".nav-btn").classList.remove("visible");
  }
});

document.querySelector(".nav-btn").addEventListener("click", function () {
  this.classList.toggle("abs");
  if (this.textContent === "x") this.textContent = "≡";
  else this.textContent = "x";
  document.querySelector(".mobile").classList.toggle("visible");
});
