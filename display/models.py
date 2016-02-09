from django.db import models


class Article(models.Model):
    author = models.CharField(max_length=50)
    pub_date = models.DateField('publish date')
    text = models.TextField()


