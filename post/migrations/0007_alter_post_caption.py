# Generated by Django 5.1.3 on 2025-02-23 14:48

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_delete_postcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text'),
        ),
    ]
