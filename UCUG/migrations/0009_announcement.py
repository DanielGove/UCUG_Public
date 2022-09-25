# Generated by Django 3.2.9 on 2022-09-25 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UCUG', '0008_alter_user_profile_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, null=True)),
                ('content', models.TextField()),
                ('created_UTC', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
