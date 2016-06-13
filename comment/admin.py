from django.contrib import admin

# Register your models here.
from models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ("block", "article", "content", "owner", "status", "last_update_timestamp")
    list_filter = ("block", )
    search_fields = ("content", )

admin.site.register(Comment, CommentAdmin)
