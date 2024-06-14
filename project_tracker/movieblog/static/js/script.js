const navItems = document.querySelectorAll('.navbar__item');
const currentUrl = window.location.href;

navItems.forEach(item => {
  if (item.href === currentUrl) {
    item.classList.add('active');
  }
});



document.getElementById('toggleButton').addEventListener('click', function() {    
    if (document.body.classList.contains('dark-theme')) {
        document.body.classList.remove('dark-theme');
        document.body.classList.add('light-theme');
    } else {
        document.body.classList.remove('light-theme');
        document.body.classList.add('dark-theme');
    }
  });
  