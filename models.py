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

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return "/%s" % self.slug

    def get_post_content(self):
        dbx = dropbox.Dropbox(settings.DROPBOX_TOKEN)

        directory = self.date_published.strftime("%Y")
        filename = self.post_filename

        meta, file = dbx.files_download('/%s/%s.md' % (directory, filename))
        file_content = file.content

        return file_content
