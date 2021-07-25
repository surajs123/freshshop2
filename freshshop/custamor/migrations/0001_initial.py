# Generated by Django 3.2 on 2021-07-25 05:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='onlineuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('user_name', models.CharField(max_length=100)),
                ('first_name', models.CharField(blank=True, default=False, max_length=100)),
                ('last_name', models.CharField(blank=True, default=False, max_length=100)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('gender', models.CharField(blank=True, default=False, max_length=100)),
                ('address', models.TextField(blank=True, default=False, max_length=200)),
                ('place', models.CharField(blank=True, default=False, max_length=100)),
                ('pincode', models.IntegerField(blank=True, default=0)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
