from django.contrib import admin

# Register your models here.
from models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("owner", "avatar", "create_timestamp", "last_update_timestamp")


admin.site.register(UserProfile, UserProfileAdmin)
