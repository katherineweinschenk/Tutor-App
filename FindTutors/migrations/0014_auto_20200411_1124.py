# Generated by Django 3.0.3 on 2020-04-11 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FindTutors', '0013_auto_20200411_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', upload_to='profile_pictures'),
        ),
    ]
