# Generated by Django 4.2.7 on 2023-12-05 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0002_rename_converstion_conversation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversationmessage',
            old_name='converstion',
            new_name='conversation',
        ),
    ]
