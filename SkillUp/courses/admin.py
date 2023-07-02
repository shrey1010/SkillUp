from django.contrib import admin
from .models.course import Course,Tag,Prerequisite,Learning
from .models.payment import Payment
from .models.user_course import UserCourse
from.models.video import Video
# Register your models here.

class TagAdmin(admin.TabularInline):
    model = Tag


class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite


class LearningAdmin(admin.TabularInline):
    model = Learning


class VideoAdmin(admin.TabularInline):
    model = Video


class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin, PrerequisiteAdmin,LearningAdmin,VideoAdmin]


admin.site.register(Course,CourseAdmin)
admin.site.register(Video)
admin.site.register(Payment)
admin.site.register(UserCourse)
