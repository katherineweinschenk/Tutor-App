# Generated by Django 3.0.2 on 2020-03-01 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FindTutors', '0002_auto_20200301_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='tuser',
            name='username',
            field=models.CharField(default='0', max_length=200),
        ),
    ]
