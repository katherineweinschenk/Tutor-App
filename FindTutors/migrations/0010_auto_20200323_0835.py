# Generated by Django 3.0.2 on 2020-03-23 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FindTutors', '0009_auto_20200323_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, default=' '),
        ),
    ]
