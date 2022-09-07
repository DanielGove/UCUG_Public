# Generated by Django 4.0.4 on 2022-04-19 01:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UCUG', '0003_auto_20211211_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='private_message',
            name='from_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_from_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='private_message',
            name='to_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_to_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
