# Generated by Django 5.0.4 on 2024-06-07 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Homes', '0014_job_files'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='files',
        ),
    ]