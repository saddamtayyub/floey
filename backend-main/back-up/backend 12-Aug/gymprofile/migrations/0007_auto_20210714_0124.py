# Generated by Django 3.2 on 2021-07-14 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymprofile', '0006_auto_20210712_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='class_address',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='classes',
            name='class_gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Unisex', 'Unisex')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_address',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Unisex', 'Unisex')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='gymprofile',
            name='gym_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]