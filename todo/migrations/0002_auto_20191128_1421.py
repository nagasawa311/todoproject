# Generated by Django 2.2.7 on 2019-11-28 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TodoList',
            new_name='TodoModel',
        ),
    ]
