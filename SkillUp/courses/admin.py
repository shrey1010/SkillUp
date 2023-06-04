from django.contrib import admin
from .models import Course,Tag,Prerequisites,Learning
# Register your models here.

class TagAdmin(admin.TabularInline):
    model = Tag


class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisites


class LearningAdmin(admin.TabularInline):
    model = Learning


class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin, PrerequisiteAdmin,LearningAdmin]


admin.site.register(Course,CourseAdmin)
