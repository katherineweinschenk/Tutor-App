# Generated by Django 3.0.3 on 2020-04-07 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FindTutors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tuser',
            name='image',
            field=models.ImageField(default='default.png', upload_to='tutor_profile/'),
        ),
    ]
