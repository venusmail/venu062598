# Generated by Django 4.2.7 on 2023-12-22 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('email_tracking_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trackedclick',
            old_name='dropp',
            new_name='drop',
        ),
        migrations.RenameField(
            model_name='unsub',
            old_name='dropp',
            new_name='drop',
        ),
    ]
