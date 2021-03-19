from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __repr__(self):
        return f'<{type(self).__name__}({self.username})>'

    def __str__(self):
        return self.username
