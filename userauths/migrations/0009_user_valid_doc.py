# Generated by Django 5.1.3 on 2025-02-06 11:14

import userauths.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0008_alter_user_account_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='valid_doc',
            field=models.FileField(default='', upload_to=userauths.models.user_directory_path),
            preserve_default=False,
        ),
    ]
