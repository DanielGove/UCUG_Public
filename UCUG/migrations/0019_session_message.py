# Generated by Django 4.1.1 on 2022-11-04 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UCUG', '0018_remove_forum_owner_remove_post_owner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='message',
            field=models.CharField(max_length=24, null=True),
        ),
    ]
