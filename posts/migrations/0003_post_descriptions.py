# Generated by Django 2.2.1 on 2019-05-09 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("posts", "0002_post_content")]

    operations = [
        migrations.AddField(
            model_name="post",
            name="descriptions",
            field=models.TextField(default="", max_length=600),
        )
    ]
