// Получаем все элементы меню
const navItems = document.querySelectorAll('.navbar__item');
// Получаем текущий URL
const currentUrl = window.location.href;

navItems.forEach(item => {
  // Если href элемента совпадает с текущим URL, добавляем класс active
  if (item.href === currentUrl) {
    item.classList.add('active');
  }
});
