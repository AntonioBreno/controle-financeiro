const toggleBtn = document.getElementById("toggleBtn");
const layout = document.getElementById("layout");

toggleBtn.addEventListener("click", () => {
  layout.classList.toggle("collapsed");
});