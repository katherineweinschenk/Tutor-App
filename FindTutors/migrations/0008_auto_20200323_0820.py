# Generated by Django 3.0.2 on 2020-03-23 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FindTutors', '0007_auto_20200323_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pictures/'),
        ),
    ]
