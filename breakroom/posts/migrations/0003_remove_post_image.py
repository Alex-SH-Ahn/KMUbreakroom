# Generated by Django 5.0.4 on 2024-05-11 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
