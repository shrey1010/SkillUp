from django.db import models
from .course import Course
# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=100,null = False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,null = False)
    description = models.TextField(blank = True, max_length=50)
    serial_number = models.IntegerField(null=False)
    video_id = models.CharField(max_length=50,null = False)
    is_preview = models.BooleanField(default=False)

