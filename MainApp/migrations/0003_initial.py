# Generated by Django 4.1.1 on 2023-04-20 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('MainApp', '0002_delete_userdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('pin', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('mode', models.CharField(max_length=30)),
            ],
        ),
    ]
