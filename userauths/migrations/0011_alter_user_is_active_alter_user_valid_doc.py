# Generated by Django 5.1.3 on 2025-02-06 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0010_profile_student_type_profile_year_of_join_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='valid_doc',
            field=models.FileField(upload_to='valid_proof/'),
        ),
    ]
