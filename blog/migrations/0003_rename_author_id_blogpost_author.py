# Generated by Django 4.1.6 on 2023-02-23 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_author_name_comment_author_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='author_id',
            new_name='author',
        ),
    ]
