# Generated by Django 5.2 on 2025-06-22 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
    ]
