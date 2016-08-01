#import Django's function URL and all of our views from blog1 application.
from django.conf.urls import url
from . import views

urlpatterns = [
    #First URL pattern
    url(r'^$', views.post_list, name='post_list'),
]
""" assign a view called 'post_list' to '^$' URL.
        This Regular Expression will match '^" (a beginning)
        followed by '$' (the end) - therefore only an Empty String
        will match.

        This pattern tells Django that 'views.post_list' is the right place
        to go if someone enters your website at address 'http://127.0.0.1:8000/

        'name='post_list'' is the URL name used to identify the view.
        -can be the same name of the view or different."""


