from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100,null = False)
    description = models.TextField()
    price = models.IntegerField(default = 0,null=False)
    discount = models.IntegerField(default =0)
    active = models.BooleanField(default = False)
    date = models.DateTimeField(auto_now_add=True)
    length = models.IntegerField(default = 0,null = False)
    thumbnail = models.ImageField(upload_to="files/thumbnail",null=False)
    resources = models.FileField(upload_to="files/resources", null=False)

class CourseProperty(models.Model):
    description = models.CharField(max_length=255,null = False)
    course = models.ForeignKey(Course,null=False,on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Tag(CourseProperty):
    pass

class Prerequisites(CourseProperty):
    pass

class Learning(CourseProperty):
    pass


