# Online_cinema
This is a thesis for the course "Web developer"
Главная страница по адресу
http://127.0.0.1:8000/movieblog/18-vse-filmy/
Username (leave blank to use 'mme06'): our_user 
Password: ouruser

# Настройка почты
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'movieblogtest@yandex.ru'
EMAIL_HOST_PASSWORD = 'm;QT-Z4^P%8Naa!'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

