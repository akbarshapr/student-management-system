# Generated by Django 4.1.7 on 2023-03-16 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0002_remove_assignment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='department',
        ),
    ]
