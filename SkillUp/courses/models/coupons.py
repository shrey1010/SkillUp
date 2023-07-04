from django.db import models
from courses.models import Course
from courses.models import UserCourse
from django.contrib.auth.models import User



class Coupon(models.Model):
    code = models.CharField(max_length=10)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name="coupons")
    discount = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

