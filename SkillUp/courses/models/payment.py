from django.db import models
from courses.models import Course
from django.contrib.auth.models import User
from courses.models import UserCourse

class Payment(models.Model):
    order_id = models.CharField(max_length=50,null = False)
    payment_id = models.CharField(max_length=50)
    user_course = models.ForeignKey(UserCourse,null=True,blank=True,on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.User.username
