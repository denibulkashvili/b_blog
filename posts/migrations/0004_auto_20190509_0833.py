# Generated by Django 2.2.1 on 2019-05-09 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("posts", "0003_post_descriptions")]

    operations = [
        migrations.RenameField(
            model_name="post", old_name="descriptions", new_name="description"
        )
    ]
