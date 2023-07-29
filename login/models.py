from django.contrib.auth.models import User
from django.db import models


class AbstractModel(models.Model):
    updated_date=models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name='update_date',
    )
    created_date=models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name='created_date',
    )
    class Meta:
        abstract = True

class Login_User(AbstractModel):
    username = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='username',


    )
    password = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='password',

    )
    profile_img=models.ImageField(
        default='{% get_media_prefix %}images/logo/blank_profile_image.png',
        help_text='',
        verbose_name='Image',
        blank=True,
        upload_to="profile_img"

    )

    def __str__(self):
        return f"Login Settings {self.username}"
    class Meta:
        verbose_name = "Login Settings"
        verbose_name_plural = "Login Settings"
        ordering = ('username','password')