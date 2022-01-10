from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):
    
    def create_user(self, email, user_name, first_name, password, **kwargs):
        print(kwargs)
        if not email:
            raise ValueError(_('Provide email!'))
        kwargs.setdefault('is_active', True)
        email = self.normalize_email(email) 
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, user_name, first_name, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        
        return self.create_user(email, user_name, first_name, password, **kwargs)


class NewUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email addres'), unique=True)
    user_name = models.CharField(max_length=250, unique=True)
    first_name = models.CharField(max_length=200, blank=True)
    start_date = models.DateField(default=timezone.now)
    about = models.TextField(_('about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name', 'about']

    def __str__(self):
        return self.user_name
