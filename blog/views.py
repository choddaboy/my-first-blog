from django.shortcuts import render
from django.utils import timezone
#include model Post: (the . before models means: "current directory/application"
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

"""post_list(request): function we created that takes [request] and returns a function
render().

posts: variable for QuerySet

 render(request, 'blog/post_list.html', {}): a function that will render our template ( blog/post_list.html)
 {}: a place we can add things for the template to use


"""

