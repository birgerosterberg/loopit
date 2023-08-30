// Automagic close of the messages displayed.
setTimeout(function () {
  let messages = document.getElementById("msg");
  let alert = new bootstrap.Alert(messages);
  alert.close();
}, 2500);

document.addEventListener("DOMContentLoaded", (event) => {
  const urlParams = new URLSearchParams(window.location.search);
  const category = urlParams.get("category") || "All";

  document.querySelectorAll(".category-link").forEach((link) => {
    const linkCategory = link.textContent;
    if (linkCategory === category) {
      link.classList.add("active");
    } else {
      link.classList.remove("active");
    }
  });
});
