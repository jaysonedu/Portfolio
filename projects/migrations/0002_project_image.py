# Generated by Django 5.0.6 on 2024-07-08 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.FileField(blank=True, upload_to='project_images/'),
        ),
    ]
