# Generated by Django 4.2.7 on 2023-12-05 15:44

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_alter_item_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('conversation', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Converstion',
            new_name='Conversation',
        ),
    ]