// Toggle collapsible menu
const toggleMenuButton = document.getElementById("toggleMenu");
const leftMenu = document.getElementById("leftMenu");
const toggleButton = document.getElementById("togglebutton");

toggleMenuButton.addEventListener("click", () => {
  leftMenu.classList.toggle("collapsed");
  toggleButton.classList.toggle("closed");
});

// Function to adjust layout based on screen width
function adjustLayout() {
  const screenWidth = window.innerWidth; // Get the screen width
  const mainContainer = document.querySelector(".main-container"); // Select the main container

  // Apply scaling based on screen width
  if (screenWidth >= 992 && screenWidth <= 1600) {
    mainContainer.style.transform = "scale(0.9)";
    mainContainer.style.transformOrigin = "top";
  } else if (screenWidth >= 700 && screenWidth <= 767) {
    mainContainer.style.transform = "scale(0.8)";
    mainContainer.style.transformOrigin = "top";
  } else if (screenWidth >= 600 && screenWidth <= 700) {
    mainContainer.style.transform = "scale(0.75)";
    mainContainer.style.transformOrigin = "top";
  } else if (screenWidth <= 600) {
    mainContainer.style.transform = "scale(0.5)";
    mainContainer.style.transformOrigin = "top";
  } else {
    mainContainer.style.transform = "scale(1)"; // Default scale
  }
}

// Add event listener to adjust layout on page load and window resize
window.addEventListener("DOMContentLoaded", adjustLayout); // Trigger on page load
window.addEventListener("resize", adjustLayout); // Trigger on window resize
