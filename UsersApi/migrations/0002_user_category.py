# Generated by Django 3.2.11 on 2022-01-10 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UsersApi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='category',
            field=models.CharField(default='normaluser', max_length=50),
        ),
    ]
