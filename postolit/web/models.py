from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

# <Для аутентификации с помощью сессий (НЕ встроенной в Django)>
'''class User(models.Model):
    login = models.CharField(unique=True, max_length=128)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=128)

class Session(models.Model):
    key = models.CharField(unique=True, max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expires = models.DateTimeField() # время жизни сессии'''
# </Для аутентификации с помощью сессий (НЕ встроенной в Django)>


# <Для аутентификации с помощью сессий (встроенной в Django)>

User = get_user_model()