# Generated by Django 5.0 on 2023-12-18 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlmodel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='experience1',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='feature',
            name='experience2',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='feature',
            name='experience3',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='feature',
            name='experience',
            field=models.FloatField(default=0),
        ),
    ]
