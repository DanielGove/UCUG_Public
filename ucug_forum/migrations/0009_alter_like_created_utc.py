# Generated by Django 4.1.1 on 2022-12-12 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ucug_forum', '0008_alter_like_created_utc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='created_UTC',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
