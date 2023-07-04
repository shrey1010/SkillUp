from django.utils.html import format_html
from django.contrib import admin
from .models.course import Course,Tag,Prerequisite,Learning
from .models.payment import Payment
from .models.user_course import UserCourse
from.models.video import Video
from courses.templatetags import custom_tags
from .models.coupons import Coupon
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
    list_display = ["name","get_price","get_discount","active"]
    list_filter = ["discount","active","price"]

    def get_discount(self,course):
        return f"{course.discount}%"
    
    get_discount.short_description = "discount"
    
    def get_price(self, course):   
        return custom_tags.rupee(course.price)
    
    get_price.short_description = "MRP price"

class Payment_admin(admin.ModelAdmin):
    model = Payment
    list_display = ["order_id", 'get_user', 'get_course', 'status']
    list_filter = ["status", 'course']

    def get_user(self, payment):
        return format_html(f"<a target='_blank' href='/admin/auth/user/{payment.user.id}'>{payment.user}</a>")

    def get_course(self, payment):
        return format_html(f"<a target='_blank' href='/admin/courses/course/{payment.course.id}'>{payment.course}</a>")

    get_course.short_description = "Course"
    get_user.short_description = "User"


class UserCourseAdmin(admin.ModelAdmin):
    model = UserCourse
    list_display = ['click', 'get_user', 'get_course']
    list_filter = ['course']

    def get_user(self, usercourse):
        return format_html(f"<a target='_blank' href='/admin/auth/user/{usercourse.user.id}'>{usercourse.user}</a>")

    def click(self, usercourse):
        return "Click to Open"

    def get_course(self, usercourse):
        return format_html(f"<a target='_blank' href='/admin/courses/course/{usercourse.course.id}'>{usercourse.course}</a>")

    get_course.short_description = "Course"
    get_user.short_description = "User"


class CouponAdmin(admin.ModelAdmin):
    model = Coupon
    list_display = ["code","course","discount","is_active"]

admin.site.register(Course,CourseAdmin)
admin.site.register(Video)
admin.site.register(Coupon,CouponAdmin)
admin.site.register(Payment,Payment_admin)
admin.site.register(UserCourse,UserCourseAdmin)
