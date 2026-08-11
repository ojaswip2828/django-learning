from django.db import models


class UrlData(models.Model):
    url = models.URLField(max_length=200)
    slug = models.CharField(max_length=10)

    def __str__(self):
        return f"Short URL for: {self.url} is {self.slug}"