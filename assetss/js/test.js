let isMenuExpanded = false;

function toggleMenu() {
  const menu = document.getElementById('menu');

  if (isMenuExpanded) {
    menu.classList.remove('expanded');
    menu.classList.add('collapsed');
  } else {
    menu.classList.remove('collapsed');
    menu.classList.add('expanded');
  }

  isMenuExpanded = !isMenuExpanded;
}
