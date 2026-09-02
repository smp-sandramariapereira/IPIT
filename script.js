const menuButton = document.querySelector(".menu-toggle");
const menu = document.querySelector("#menu-principal");

function closeMenu({ returnFocus = false } = {}) {
  menuButton?.setAttribute("aria-expanded", "false");
  menu?.classList.remove("is-open");
  if (returnFocus) menuButton?.focus();
}

menuButton?.addEventListener("click", () => {
  const willOpen = menuButton.getAttribute("aria-expanded") !== "true";
  menuButton.setAttribute("aria-expanded", String(willOpen));
  menu.classList.toggle("is-open", willOpen);
});

menu?.addEventListener("click", (event) => {
  if (event.target instanceof HTMLAnchorElement) closeMenu();
});

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && menu?.classList.contains("is-open")) closeMenu({ returnFocus: true });
});
