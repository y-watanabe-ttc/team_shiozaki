# Generated by Django 2.2.2 on 2019-06-26 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0003_remove_post_quote'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='quote',
            field=models.IntegerField(null=True, verbose_name='引用ID'),
        ),
    ]