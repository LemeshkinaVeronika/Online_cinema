from django.urls import path  

from user_app import views  
from django.contrib.auth import views as auth_views  
from django.urls import reverse_lazy

app_name = 'user_app'  
urlpatterns = [  
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user_app/logout.html'), name='logout'), 
    path('signup/', views.CustomRegistrationView.as_view(), name='signup'), 
    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),  
    path('password_reset_confirm/<uidb64>/<token>/', views.CustomUserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),  
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='user_app/password_reset_complete.html'), name='password_reset_complete'),  
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='user_app/password_reset_done.html'), name='password_reset_done'),
    path('<str:username>/', views.UserProfileView.as_view(), name='user_profile'),
    path('<str:username>/settings/', views.UserSettingsView.as_view(), name='user_profile_settings'),
  
]