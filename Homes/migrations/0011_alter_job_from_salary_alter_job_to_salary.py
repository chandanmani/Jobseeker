# Generated by Django 5.0.4 on 2024-06-01 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homes', '0010_alter_job_company_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='From_Salary',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='job',
            name='To_Salary',
            field=models.IntegerField(default=20),
        ),
    ]