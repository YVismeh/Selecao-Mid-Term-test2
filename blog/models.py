from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CategoryBlog(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="blog", default="default.jpg")
    category = models.ManyToManyField(CategoryBlog)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username