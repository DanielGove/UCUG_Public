# Generated by Django 4.1.1 on 2022-12-09 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UCUG', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='message',
            field=models.CharField(choices=[('NONE', ''), ('NO_AUTH', 'NO_AUTH'), ('BAD_INPUT', 'BAD_INPUT')], default='NONE', max_length=16),
        ),
    ]