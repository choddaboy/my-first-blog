from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})

"""post_list(request): function we created that takes [request] and returns a function
render().
 render(request, 'blog/post_list.html', {}): a function that will render our template ( blog/post_list.html)
"""

