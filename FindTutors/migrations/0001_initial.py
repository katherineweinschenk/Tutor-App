# Generated by Django 3.0.2 on 2020-04-01 22:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pictures')),
                ('year', models.CharField(choices=[('1st', 'First Year'), ('2nd', 'Second Year'), ('3rd', 'Third Year'), ('4th', 'Fourth Year')], default='1st', max_length=3)),
                ('user_type', models.CharField(choices=[('1st', 'Tutor'), ('2nd', 'Tutee'), ('3rd', 'Tutor and Tutee')], default='tutor', max_length=15)),
                ('subjects', models.CharField(default='', max_length=500)),
                ('bio', models.TextField(default=' ')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(default='0', max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('image', models.ImageField(default='default.png', upload_to='tutor_profile')),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('is_tutee', models.BooleanField(default=False, verbose_name='student status')),
                ('is_tutor', models.BooleanField(default=False, verbose_name='teacher status')),
                ('year', models.IntegerField(blank=True, null=True)),
                ('subjects', models.CharField(default='', max_length=500)),
                ('bio', models.TextField(default=' ')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviews', models.TextField(default=' ')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FindTutors.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default='', max_length=500)),
                ('description', models.CharField(default='', max_length=500)),
                ('location', models.CharField(default='', max_length=500)),
                ('recipient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='TUser_recipient', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='TUser_sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
