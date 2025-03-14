# Generated by Django 5.1.3 on 2025-02-06 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0009_user_valid_doc'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='student_type',
            field=models.CharField(choices=[('Junior', 'Junior'), ('Under Graduate', 'Under Graduate'), ('Post Graduate', 'Post Graduate')], default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='year_of_join',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='year_of_passout',
            field=models.DateField(blank=True, null=True),
        ),
    ]
