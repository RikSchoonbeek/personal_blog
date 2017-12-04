from django.shortcuts import render

from .models import Category, Post

# Create your views here.
def show_posts(request, category='', timestamp=''):
    posts = Post.objects.all()
    categories = Category.objects.all()
    # If category is added, filter by category
    if len(category) > 0:
        posts.filter(category=category)
    # If timestamp is added, filter by timestamp
    if len(timestamp) > 0:
        # Filter for timestamp
        pass

    return render(request, 'blog/show_posts.html', {'posts': posts,
                                                    'categories': categories})
