# Generated by Django 2.2.1 on 2019-05-10 04:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("posts", "0005_auto_20190509_2337")]

    operations = [
        migrations.AlterModelOptions(
            name="post", options={"ordering": ["-date_created"]}
        ),
        migrations.AlterModelOptions(name="tag", options={"ordering": ["name"]}),
        migrations.AddField(
            model_name="post",
            name="content_html",
            field=models.TextField(default="", editable=False),
        ),
        migrations.AddField(
            model_name="post",
            name="cover",
            field=models.ImageField(default="covers/default.jpg", upload_to="covers/"),
        ),
        migrations.AddField(
            model_name="post",
            name="date_created",
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name="post",
            name="is_featured",
            field=models.BooleanField(default=False),
        ),
    ]
