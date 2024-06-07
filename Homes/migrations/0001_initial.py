# Generated by Django 5.0.4 on 2024-04-21 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Homes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_name', models.CharField(max_length=30)),
                ('house_price', models.IntegerField()),
                ('house_description', models.TextField()),
                ('house_image', models.ImageField(upload_to='Homes/')),
            ],
        ),
    ]
