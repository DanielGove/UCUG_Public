# Generated by Django 3.2.9 on 2022-12-07 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ucug_forum', '0002_auto_20221206_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='mentions',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mention', to='ucug_forum.post'),
        ),
    ]