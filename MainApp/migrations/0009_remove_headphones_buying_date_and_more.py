# Generated by Django 4.1.1 on 2023-04-27 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0008_headphones'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='headphones',
            name='buying_date',
        ),
        migrations.RemoveField(
            model_name='headphones',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='headphones',
            name='image3',
        ),
    ]
