from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=30) # 최대 글자수 필수로 정해줘야 한다.
    content = models.TextField()

    def __str__(self):
        return self.title