# Generated by Django 5.1.3 on 2025-03-17 05:30

import cloudinary.models
import django.db.models.deletion
import shortuuid.main
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(default=shortuuid.main.ShortUUID.uuid, max_length=128, unique=True)),
                ('is_private', models.BooleanField(default=False)),
                ('members', models.ManyToManyField(blank=True, related_name='chat_groups', to=settings.AUTH_USER_MODEL)),
                ('users_online', models.ManyToManyField(blank=True, related_name='online_in_groups', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroupMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(blank=True, max_length=3000, null=True)),
                ('file', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='file')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_messages', to='chat.chatgroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
