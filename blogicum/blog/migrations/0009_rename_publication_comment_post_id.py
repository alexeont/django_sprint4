# Generated by Django 3.2.16 on 2023-10-01 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20230928_2154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='publication',
            new_name='post_id',
        ),
    ]
