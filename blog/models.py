from django.utils import timezone
from django.db import models

# Create your models here. Define all objects called 'Models'

""" This is where we will define out blog post """

class Post(models.Model):  #defines our model (it is an object)
    """class- special keyword that indicates we are defining an object
    Post - the name of our model. Always start a class name with an uppercase.
    models.Model - means the Post isa Django Model. Therefor, Django will save in database.

    Below are the defined properties

    models.CharField: how you define a text with a limited # of characters
    models.TextField: for long text without a limit.
    models.DateTimeField: a date and time
    models.ForeignKey: a link to another model."""

    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)


    """def publish(self):
    def: this is a funcion/method
    publish is the name of the method.-must use lowercase and underscores for whitespace."""
    def publish(self):
        self.published_date = timezone.now()
        self.save()


    """Methods often return something.  __str__ is an example of this. When we call
    __str__() we will get a test (string) with a Post title."""
    def __str__(self):
        return self.title

