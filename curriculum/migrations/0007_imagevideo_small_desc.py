# Generated by Django 3.2.6 on 2021-08-09 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0006_auto_20210809_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagevideo',
            name='small_desc',
            field=models.CharField(default='0', max_length=200),
        ),
    ]
