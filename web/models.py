from django.db import models
from tinymce.models import HTMLField


# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=180)
    slug = models.SlugField()
    date = models.DateField(auto_now_add=True)
    description = HTMLField()

    def __str__(self):
        return self.title