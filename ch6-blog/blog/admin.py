from django.contrib import admin

from .models import Post

# Register your models here.
admin.site.register(Post)


# class PostAdmin(admin.ModelAdmin):  # Customize admin panel post list columns
#     list_display = ("title", "author", "body")


class PostAdmin(admin.ModelAdmin):  # new
    list_display = (
        "title",
        "author",
        "body",
    )
