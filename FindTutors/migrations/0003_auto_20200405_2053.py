# Generated by Django 3.0.3 on 2020-04-06 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FindTutors', '0002_auto_20200405_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='description',
            field=models.CharField(max_length=150),
        ),
    ]