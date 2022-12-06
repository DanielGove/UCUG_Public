# Generated by Django 3.2.9 on 2022-12-06 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ucug_forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='parent_post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ucug_forum.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='parent_forum',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ucug_forum.forum'),
        ),
    ]
