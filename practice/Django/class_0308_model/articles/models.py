from pickle import TRUE
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30) # 최대 글자수 필수로 정해줘야 한다.
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title