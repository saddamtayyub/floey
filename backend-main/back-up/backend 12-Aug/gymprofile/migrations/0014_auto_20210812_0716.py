# Generated by Django 3.2 on 2021-08-12 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymprofile', '0013_auto_20210811_0730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classes',
            name='class_address',
        ),
        migrations.RemoveField(
            model_name='course',
            name='course_address',
        ),
    ]
