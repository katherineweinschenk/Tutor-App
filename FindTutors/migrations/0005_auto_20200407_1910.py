# Generated by Django 3.0.3 on 2020-04-08 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FindTutors', '0004_auto_20200407_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.PositiveIntegerField(choices=[(1, 'Tutor'), (2, 'Tutee'), (3, 'Tutor and Tutee')], default=1),
        ),
    ]
