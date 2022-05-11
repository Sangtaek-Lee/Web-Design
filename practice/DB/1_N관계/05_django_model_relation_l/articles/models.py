from tkinter import CASCADE
from django.conf import settings
from django.db import models
from django.conf import settings
# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)        
    # model을 참조해서 가져오는데 settings.AUTH_USER_MODEL은 str으로 반환한다. (참조하는 이유는 수정 시 반영을 하기 위해)
    # get_user_model() 은 object로 반환한다. 근데 settings에서 installed app 을 읽을 때 순서에 따라 user 를 호출하지 못할 수도 있어 사용하지 않는다.
    # settings.AUTH_USER_MODEL 은 models.py에서만 사용한다.
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content