from distutils.command.register import register

from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('username', 'email','subscription__plan__plan_name','get_group_names')

    def get_group_names(self, obj):
        # Return a comma-separated list of group names
        return ", ".join([group.name for group in obj.groups.all()])

    search_fields = ('id','username', 'email')
