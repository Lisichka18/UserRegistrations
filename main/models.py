from django.db import models


class User(models.Model):
    name = models.CharField('Имя пользователя', max_length=255, blank=False)
    password = models.CharField('Пароль пользователя', max_length=30, blank=False)
    email = models.EmailField('Email пользователя', blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
