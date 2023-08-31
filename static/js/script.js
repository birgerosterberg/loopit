// Automagic close of the messages displayed.
// Wait for the entire HTML document to be fully loaded
document.addEventListener("DOMContentLoaded", function () {
  // Execute the following code after a delay of 2500 milliseconds (2.5 seconds)
  setTimeout(function () {
    // Select all elements with the class 'alert-message'
    let messageElements = document.querySelectorAll(".alert-message");

    // Loop through each selected element
    messageElements.forEach(function (element) {
      // Create a new bootstrap alert object for the current element
      let alert = new bootstrap.Alert(element);

      // Close the bootstrap alert
      alert.close();
    });
  }, 2500); // End of setTimeout
}); // End of DOMContentLoaded event

// Category choice magic!
// Wait for the DOM to be fully loaded before running the script
document.addEventListener("DOMContentLoaded", (event) => {
  // Create an object from the current URL's search query parameters
  const urlParams = new URLSearchParams(window.location.search);

  // Get the value of the "category" parameter from the URL, or default to "All" if it doesn't exist
  const category = urlParams.get("category") || "All";

  // Select all elements with the class 'category-link'
  document.querySelectorAll(".category-link").forEach((link) => {
    // Get the text content of each link (which should be the category name)
    const linkCategory = link.textContent;

    // Check if the category from the URL matches the category of the link
    if (linkCategory === category) {
      // If it does, add the 'active' class to highlight the link
      link.classList.add("active");
    } else {
      // Otherwise, remove the 'active' class to unhighlight the link
      link.classList.remove("active");
    }
  });
});
