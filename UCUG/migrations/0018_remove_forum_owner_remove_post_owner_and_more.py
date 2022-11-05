# Generated by Django 4.1.1 on 2022-11-04 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UCUG', '0017_announcement_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forum',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='post',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='post',
            name='parent_forum',
        ),
        migrations.RemoveField(
            model_name='private_message',
            name='from_user',
        ),
        migrations.RemoveField(
            model_name='private_message',
            name='to_user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Forum',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='private_message',
        ),
    ]