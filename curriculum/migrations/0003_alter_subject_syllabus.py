# Generated by Django 3.2.6 on 2021-08-05 07:57

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0002_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='syllabus',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
