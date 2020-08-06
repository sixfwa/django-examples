from django.contrib import admin

# Register your models here.

from .models import Post


class PostAdmin(admin.ModelAdmin):

    list_display = ("id", "content", "author", "published_date")

    list_filter = ("author",)

    list_per_page = 25


admin.site.register(Post, PostAdmin)
