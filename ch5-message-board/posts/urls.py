from django.urls import path

from .views import PostList

# urlpatterns = [path("", post_list, name="post_list")]

urlpatterns = [path("", PostList.as_view(), name="home")]
