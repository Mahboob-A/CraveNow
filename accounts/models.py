from django.db import models


from django.contrib.auth.models import AbstractBaseUser

from .managers import UserManager
from .constants import role_choices 



class User(AbstractBaseUser): 
        first_name = models.CharField(max_length=50)
        last_name = models.CharField(max_length=50)
        email = models.EmailField(max_length=100, unique=True)
        username = models.CharField(max_length=10, unique=True)
        phone_number = models.CharField(max_length=13, blank=True)
        role = models.PositiveSmallIntegerField(choices=role_choices, blank=True, null=True)
        
        # extra fields 
        date_joined = models.DateTimeField(auto_now_add=True)
        last_login = models.DateTimeField(auto_now_add=True)
        created_at = models.DateTimeField(auto_now_add=True)
        modified_at = models.DateTimeField(auto_now=True)
        
        # admin related fields 
        is_admin = models.BooleanField(default=False)
        is_staff = models.BooleanField(default=False)
        is_active = models.BooleanField(default=False)
        is_superadmin = models.BooleanField(default=False)
        
        # auth configuraion 
        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = ['first_name', 'last_name', 'username']
        
        # manager selection 
        objects = UserManager()
        
        # permission check 
        def has_perm(self, perm, obj=None): 
                return self.is_admin 
        
        def has_module_perms(self, app_label): 
                return True 
        
        # admin representation 
        def __str__(self): 
                return self.email
        