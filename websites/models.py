from email.mime import image
from turtle import title
from django.db import models

# Create your models here.
class PostModel(models.Model):
    # モデルではfieldをセット
    title = models.CharField(max_length= 50)
    memo = models.TextField()
    image = models.ImageField(upload_to = 'images', verbose_name='画像', null= True, blank= True)

    def __str__(self):
        return self.title

