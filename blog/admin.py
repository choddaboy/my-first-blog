"""Import(include) the Post model defined previously blog/models.py"""

from django.contrib import admin
from .models import Post

admin.site.register(Post) # To make Post model visible to admin, we register it with this line

# Register your models here.
