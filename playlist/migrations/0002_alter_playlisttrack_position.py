# Generated by Django 5.0.6 on 2024-06-01 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlisttrack',
            name='position',
            field=models.IntegerField(default=0),
        ),
    ]
