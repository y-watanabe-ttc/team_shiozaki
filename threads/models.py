from django.db import models

class Post(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name="名前",
        )
    message = models.CharField(
        max_length=100,
        verbose_name="コメント",
        )
    quote = models.IntegerField(
        null=True,
        verbose_name="引用ID",
        )
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="登録日時",
        )