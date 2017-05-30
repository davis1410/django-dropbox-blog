from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings

from django.utils.timezone import now

import dropbox

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    publish = models.BooleanField("Published", default=False)
    date_published = models.DateField("Date Published", default=now)
    post_filename = models.CharField("Post Filename", max_length=200)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
