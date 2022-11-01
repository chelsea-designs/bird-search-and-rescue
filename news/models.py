from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class NewsPost(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    slug = models.SlugField(max_length=128, null=False, blank=False, unique=True)
    author = models.ForeignKey(User,
                               null=False,
                               blank=False,
                               on_delete=models.SET_DEFAULT,
                               default=1)
    created_on = models.DateField(auto_now_add=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    content = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug:
            if slugify(self.title) != self.slug:
                self.slug = slugify(self.title)
        else:
            self.slug = slugify(self.title)
        super(NewsPost, self).save(*args, **kwargs)
