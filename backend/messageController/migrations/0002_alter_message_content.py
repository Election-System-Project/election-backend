# Generated by Django 4.0.10 on 2023-06-08 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messageController', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(default=' '),
        ),
    ]
