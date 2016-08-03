from django.shortcuts import render, get_object_or_404 # include model render
from .forms import PostForm #include model PostForms
from django.shortcuts import  redirect
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

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST) #if method is POST, we want to construct the PostForm with data from the Form

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
            """if the form is valid (new form to be created)
             1. form.save(commit=False): we dont want to save the form yet.
             2. this is what we want to show.
             3. Redirct: immediately fo to post_detail view after save. This view requires a pk variable,
             therefore we use pk=post.pk ( where post is the newly created blog post)
            """
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})

""" To create a new Post form, we call PostForm() from forms.py and pass it to the
template "post_edit.html" """

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
