# Generated by Django 4.1.1 on 2023-04-20 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_alter_userdetails_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='mode',
        ),
    ]
