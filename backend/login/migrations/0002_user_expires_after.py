# Generated by Django 4.0.10 on 2023-05-21 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='expires_after',
            field=models.IntegerField(default=5),
        ),
    ]
