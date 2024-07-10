from django.db import models
from datetime import datetime  
from urllib import request  
from PIL import Image  
from django.contrib.auth.models import User  
from django.db import models  
import os
from django.core.files import File
from django.conf import settings

class ProfileModel(models.Model):  
    class Genders(models.TextChoices):  
        UNDEFINED = 'U', 'не выбран'  
        MALE = 'M', 'мужской'  
        FEMALE = 'F', 'женский'  

    user = models.OneToOneField(User,  
                                on_delete=models.CASCADE,  
                                related_name='profile',  
                                verbose_name='Пользователь')  
    
    gender = models.CharField(max_length=1,  
                              choices=Genders.choices,  
                              default=Genders.UNDEFINED,  
                              verbose_name='Пол')  
    dob = models.DateField(blank=True,  
                           null=True,  
                           verbose_name='Дата рождения')  
    user_avatar = models.ImageField(upload_to='user/avatars/',  
                                    blank=True,  
                                    null=True,  
                                    verbose_name='Аватар пользователя')  

    show_email = models.BooleanField(default=False,  
                                     verbose_name='Отображать Email?')  
    show_last_name = models.BooleanField(default=False,  
                                         verbose_name='Отображать фамилию?')  
    
    class Meta:  
        verbose_name = 'Профиль'  
        verbose_name_plural = 'Профили'  

    def save(self, *args, **kwargs):  
        if not self.user_avatar:  
            default_image_path = os.path.join(settings.MEDIA_ROOT, 'film', '2024', '06', 'default_avatar.png')
            with open(default_image_path, 'rb') as f:
                self.user_avatar.save(f'{self.user.username}.png', File(f), save=False)
        
        super().save(*args, **kwargs)  

        img = Image.open(self.user_avatar.path)  

        if img.height > 300 or img.width > 300:  
            output_size = (300, 300)  
            img.thumbnail(output_size)  
            img.save(self.user_avatar.path)  
            
    def get_age(self):  
        if self.dob:  
            today = datetime.today()  
            age = today.year - self.dob.year  

            if today.month < self.dob.month:  
                age -= 1  
            elif today.month > self.dob.month and today.day < self.dob.day:  
                age -= 1  

            return age  

    def __str__(self):  
        return self.user.username
