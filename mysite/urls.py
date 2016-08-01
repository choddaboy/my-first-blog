"""mysite URL Configuration

***admin login: jayrock, superuser

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),  #for every URL that starts with admin/, Django finds a corresponding view.
 #   url(r'', include('blog.urls')), # import Blogs into the main URL ('')-anything that comes into 127.0.0.1:8000/ will be redirected to blogs.url and look for further instructions there.for
    #write regular expressions with an 'r' infront of the string. This hints to Python the string may contain special characters not meant for Python but for the Regular Expression.

]
