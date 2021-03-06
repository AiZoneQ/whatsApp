# Generated by Django 4.0.4 on 2022-07-01 14:38

from django.db import migrations, models
import wtsApi.models


class Migration(migrations.Migration):

    dependencies = [
        ('wtsApi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='fileBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(upload_to=wtsApi.models.user_directory_path)),
                ('file_id', models.IntegerField(default=-1)),
                ('sender_id', models.IntegerField(default=-1)),
            ],
        ),
    ]
