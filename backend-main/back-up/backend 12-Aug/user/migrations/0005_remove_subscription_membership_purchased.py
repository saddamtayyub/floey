# Generated by Django 3.2 on 2021-07-22 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210721_0203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='membership_purchased',
        ),
    ]
