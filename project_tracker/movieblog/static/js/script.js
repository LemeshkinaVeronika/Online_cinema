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

  
document.getElementById('wishlist').addEventListener('click', function(){
    this.classList.toggle('active-wishlist')
});
  


document.addEventListener('DOMContentLoaded', function() {
  const buttons = document.querySelectorAll('.ranks__mark');

  buttons.forEach(button => {
      button.addEventListener('click', function() {
        if (this.classList.contains('active-mark')) {
          this.classList.remove('active-mark');
        } else {
          buttons.forEach(btn => btn.classList.remove('active-mark'));
          this.classList.add('active-mark');
        }
      });
  });
});