# Generated by Django 3.2.9 on 2022-09-25 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UCUG', '0007_alter_user_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(upload_to='uploaded', verbose_name='picture'),
        ),
    ]