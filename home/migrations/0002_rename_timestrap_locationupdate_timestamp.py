# Generated by Django 5.1.1 on 2024-09-30 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='locationupdate',
            old_name='timestrap',
            new_name='timestamp',
        ),
    ]
