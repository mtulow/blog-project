from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Post


# Create your views here.

# ===
# Function views
# ===

# def index(request):
#     return HttpResponse("Hello, world. You're at the blog index.")

def posts(request):
    return HttpResponse("Hello, world. You're at the blog posts.")

def comments(request):
    return HttpResponse("Hello, world. You're at the blog comments.")



# ===
# Function views
# ===

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('created_on')
    template_name = 'index.html'

    

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
