from __future__ import unicode_literals
from django.contrib import admin
from .models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()


class UserProfileInline(admin.StackedInline):
    model = Profile


class NewUserAdmin(admin.ModelAdmin):
    inlines = [UserProfileInline]
    list_display_links = ('email',)
    list_display = ('is_active', 'email', 'is_superuser', 'is_staff',)
admin.site.unregister(User)
admin.site.register(User, NewUserAdmin)
