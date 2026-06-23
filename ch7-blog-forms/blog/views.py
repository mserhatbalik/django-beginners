from django.views.generic import DetailView, ListView

from .models import Post


# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "posts"  # Optional, in order to refer the object in templates with this variable name.


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"
