function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function showReplyForm(commentId, username) {
    var form = document.getElementById('reply-form-' + commentId);
    if (form.style.display === 'none') {
        form.style.display = 'block';
    } else {
        form.style.display = 'none';
    }
}

function toggleChildren(commentId) {
    var children = document.getElementById('children-' + commentId);
    if (children.style.display === 'none') {
        children.style.display = 'block';
    } else {
        children.style.display = 'none';
    }
}

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
  });

  
// document.getElementById('wishlist').addEventListener('click', function(){
//     this.classList.toggle('active-wishlist')
// });
  

document.addEventListener('DOMContentLoaded', function() {
  const buttons = document.querySelectorAll('.ranks__mark')
  const movie_rating = document.querySelector('.rating')

  buttons.forEach(button => {
      button.addEventListener('click', function() {
        console.log('check')
        if (this.classList.contains('active-mark')) {
          this.classList.remove('active-mark');
        } else {
          buttons.forEach(btn => btn.classList.remove('active-mark'))
          this.classList.add('active-mark');
        }

        const movieId = button.dataset.movieId
          const request = new Request(`/movieblog/rate_movie/`, {
              method: 'post',
              headers: {
                  'Content-Type': 'application/json',
                  'X-CSRFToken': getCookie('csrftoken'),
              },
              body: JSON.stringify({
                  rate_number: button.dataset.rateNumber,
                  movie_id: movieId
              })
          })
          fetch(request)
                .then((response) => {
                    if(response.status === 401) {
                        window.location.href = '/user/login'
                    }
                    else {
                        return response.json()
                    }
                })
                .then((data) => {
                    if(data.movie_rating != 0) { 
                        movie_rating.innerHTML = `Рейтинг: ${data.movie_rating}/5`;
                    }
                    else {
                        movie_rating.innerHTML = "Рейтинг: Слишком мало оценок"
                    }
                    console.log(data.movie_rating)
                })
      });
  });
});
