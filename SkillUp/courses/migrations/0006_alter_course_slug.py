# Generated by Django 4.1.5 on 2023-06-29 10:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0005_course_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="slug",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
