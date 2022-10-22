from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class TeamMember(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    slug = models.SlugField(max_length=128, null=False, blank=False, unique=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    biography = models.TextField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug:
            if slugify(self.name) != self.slug:
                self.slug = slugify(self.name)
        else:
            self.slug = slugify(self.name)
        super(TeamMember, self).save(*args, **kwargs)
