from django.contrib import admin
from .custom_user import CustomUserAdmin
from ..models import CustomUser

admin.site.register(CustomUser, CustomUserAdmin)
