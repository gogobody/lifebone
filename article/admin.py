# coding: utf-8
from django.contrib import admin

from comment.models import Comment
from models import Article


class CommentInline(admin.TabularInline):
    model = Comment
    readonly_fields = ("owner", "content", "status", "create_timestamp")
    fieldsets = (
        (None, {
            "fields": ("owner", "content", "status", "create_timestamp")
        }),
    )
CommentInline.can_delete = False
CommentInline.max_num = 20
CommentInline.min_num = 0


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "block", "owner", "status", "create_timestamp", "last_update_timestamp")
    search_fields = ["title", "content", "owner"]
    list_filter = ("block", )
    actions = ["make_picked"]
    inlines = [CommentInline]
    readonly_fields = ("title", "block", "owner", "content", "status", "create_timestamp", "last_update_timestamp")
    fieldsets = (
        (None, {
            "fields": ("title", "owner", "content", "status", "create_timestamp")
        }),
        (u"其他的", {
            "classes": ('collapse',),
            "fields": ("block", "last_update_timestamp")
        }),
    )

    def make_picked(modeladmin, request, queryset):
        for a in queryset:
            a.status = 10
            a.save()
    make_picked.short_description = u"设置精华"

admin.site.register(Article, ArticleAdmin)
