# Generated by Django 4.1.5 on 2023-06-06 09:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0002_video_tag_prerequisites_learning"),
    ]

    operations = [
        migrations.AddField(
            model_name="video",
            name="description",
            field=models.TextField(blank=True, max_length=50),
        ),
    ]
