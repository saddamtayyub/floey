# Generated by Django 3.2 on 2021-08-11 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymprofile', '0012_alter_gymprofile_gym_theme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course_description',
        ),
        migrations.AddField(
            model_name='course',
            name='no_of_classes',
            field=models.IntegerField(default=10),
        ),
    ]
