from django.contrib import admin
from .models.course import Course,Tag,Prerequisites,Learning
from.models.video import Video
# Register your models here.

class TagAdmin(admin.TabularInline):
    model = Tag


class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisites


class LearningAdmin(admin.TabularInline):
    model = Learning


class VideoAdmin(admin.TabularInline):
    model = Video


class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin, PrerequisiteAdmin,LearningAdmin,VideoAdmin]


admin.site.register(Course,CourseAdmin)
