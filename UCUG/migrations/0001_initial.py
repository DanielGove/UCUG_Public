# Generated by Django 3.2.3 on 2021-12-11 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_UTC', models.DateTimeField(auto_now_add=True)),
                ('updated_UTC', models.DateTimeField(auto_now=True)),
                ('owner', models.BigIntegerField(null=True)),
                ('parent_post', models.BigIntegerField(editable=False, null=True)),
                ('content', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_UTC', models.DateTimeField(auto_now_add=True)),
                ('updated_UTC', models.DateTimeField(auto_now=True)),
                ('owner', models.BigIntegerField(null=True)),
                ('description', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_UTC', models.DateTimeField(auto_now_add=True)),
                ('updated_UTC', models.DateTimeField(auto_now=True)),
                ('owner', models.BigIntegerField(null=True)),
                ('parent_forum', models.BigIntegerField(editable=False, null=True)),
                ('content', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='private_message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_UTC', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('from_user', models.BigIntegerField(null=True)),
                ('to_user', models.BigIntegerField()),
                ('subject', models.CharField(max_length=32)),
                ('content', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_UTC', models.DateTimeField(auto_now_add=True)),
                ('ip', models.GenericIPAddressField()),
                ('method', models.CharField(max_length=8)),
                ('route', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=64, null=True, unique=True, verbose_name='username')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='is_superuser')),
                ('is_staff', models.BooleanField(default=False)),
                ('joined', models.DateTimeField(auto_now_add=True, verbose_name='joined')),
                ('last_activity', models.DateTimeField(auto_now=True, verbose_name='last_active')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
