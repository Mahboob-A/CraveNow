from django.contrib import admin

from django.contrib.auth.admin import UserAdmin  # this UseraAdmin will make the password field non-editalble 

from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin): 
        list_display = ['email', 'username', 'first_name', 'last_name', 'is_admin', 'role']
        ordering = ['-date_joined']        
        filter_horizontal = ()
        list_filter = ()
        fieldsets = ()

# admin.site.register(User, CustomUserAdmin)