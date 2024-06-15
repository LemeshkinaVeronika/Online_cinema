const navItems = document.querySelectorAll('.navbar__item');
const currentUrl = window.location.href;

navItems.forEach(item => {
  if (item.href === currentUrl) {
    item.classList.add('active');
  }
});



document.getElementById('theme-switcher').addEventListener('click', function() {    
    if (document.getElementById('theme-switcher').checked)  {
        document.body.classList.remove('dark-theme');
        document.body.classList.add('light-theme');
    } else {
        document.body.classList.remove('light-theme');
        document.body.classList.add('dark-theme');
    }
    console.log("Something happend")
  });
  