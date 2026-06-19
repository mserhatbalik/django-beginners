from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):  # Change the fields shown in admin panel post view
    list_display = (
        "title",
        "author",
        "body",
    )


# Register your models here.
admin.site.register(Post, PostAdmin)
