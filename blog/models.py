from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse_lazy

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(
                settings.AUTH_USER_MODEL,
                on_delete=models.CASCADE,
                )
    slug = models.SlugField(max_length=49, unique=True)
    publish_datetimestamp = models.DateTimeField(auto_now_add=True)
    edited_datetimestamp = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse_lazy('blog:detail', kwargs={'username': self.author.username,
                                            'slug': self.slug})

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        slug = slugify(self.title[:50])
        count = self.__class__.objects.filter(
                author=self.author,
                slug__startswith=slug).count()
        self.slug = slug

        if count > 0:
            self.slug = slug + str(count)

        super().save(*args, **kwargs)
