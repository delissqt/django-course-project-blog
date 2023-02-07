from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

from datetime import date

from .models import Post
    

# Create your views here.

def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", { "posts": latest_posts })

class StartingPage(ListView):
    template_name = "blog/index.html"
    model = Post.objects.all().order_by("-date")[:3]
    context_object_name = "posts"


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", { "all_posts": all_posts })

class Posts(ListView):
    template_name = "blog/all-posts.html"
    model = Post.objects.all().order_by("-date")
    context_name = all_posts


def post_detail(request, slug):
    #identified_post = Post.objects.get(slug=slug)
    identified_post =get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tag.all() # get all tags related to this post
        })
        # we are querying for all the related tags


class PostDetailView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_view = self.object
        request = self.request
        post_slug = Post.objects.get(slug= kwargs.slug)
        context["post"] = post_slug
        context["post_tags"] = post_slug.tag.all() 
 