from distutils.command.register import register

from django.contrib import admin

from .models import Profile


# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('user__username', 'user__email')
    search_fields = ('user__id','user__username', 'user__emai')