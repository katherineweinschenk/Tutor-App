# Generated by Django 3.0.2 on 2020-03-28 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FindTutors', '0015_tuser_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tuser',
            name='bio',
            field=models.TextField(default=' '),
        ),
    ]
