from django.views.generic import CreateView, DetailView, ListView, UpdateView

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


class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]
