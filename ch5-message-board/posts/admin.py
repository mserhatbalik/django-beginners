from django.contrib import admin

# Register your models here.
from .models import Post

# Make Post table available to admin
admin.site.register(Post)
