# Generated by Django 3.2.20 on 2023-08-20 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_post_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on']},
        ),
    ]
