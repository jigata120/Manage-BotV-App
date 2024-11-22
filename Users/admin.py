from distutils.command.register import register

from django.contrib import admin

from .models import Profile


# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('username', 'email','subscription__plan__plan_name')
    search_fields = ('id','username', 'email')
