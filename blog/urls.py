

#import Django's function URL and all of our views from blog1 application.
from django.conf.urls import url
from . import views


urlpatterns = [
    #First URL pattern
    url(r'^$', views.post_list, name='post_list'), #comment 1.

    #URL to point to a view names post_detail
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'), #comment 2.

]
"""  Comment 1:
        assign a view called 'post_list' to '^$' URL.
        This Regular Expression will match '^" (a beginning)
        followed by '$' (the end) - therefore only an Empty String
        will match.

        This pattern tells Django that 'views.post_list' is the right place
        to go if someone enters your website at address 'http://127.0.0.1:8000/

        'name='post_list'' is the URL name used to identify the view.
        -can be the same name of the view or different.

    Comment 2:
        ^post/(?P<pk>\d+)/$:
        1. ^: beginning of text
        2. post/: after the beginning the URL should contain the word POST and /
        3. (?P<pk>\d+): Django will take everything here and transfer is to a view
                        as a variable (pk) primary key.
                        \d: it can only be a digit (0-9)
                        +:  there needs to be one or more digit there.
        4. /: need another /
        5. $: the end.



        """


