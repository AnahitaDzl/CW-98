from django.db import models
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'title: {self.title} | author: {self.author} | publish date: {self.date}'
class Author(models.Model):
    pass

class Comment(models.Model):
    pass
