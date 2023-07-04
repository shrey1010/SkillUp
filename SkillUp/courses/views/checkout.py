from django.shortcuts import render, redirect
from courses.models import Course, Video, Payment, UserCourse,Coupon
from django.shortcuts import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from SkillUp.settings import *
from time import time

import razorpay
client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))


@login_required(login_url='/login')
def checkout(request, slug):
    course = Course.objects.get(slug=slug)
    user = request.user
    action = request.GET.get('action')
    
    
    order = None
    payment = None
    error = None
    try:
        user_course = UserCourse.objects.get(user=user, course=course)
        error = "You are Already Enrolled in this Course"
    except:
        pass
    amount = None
    if error is None:
        amount = int(
            (course.price - (course.price * course.discount * 0.01)) * 100)
   # if ammount is zero dont create paymenty , only save emrollment obbect
    coupon_code_messege = None
    couponcode = request.GET.get('couponcode')
    coupon = None
    if couponcode :
        try:
            coupon = Coupon.objects.get(code=couponcode, course=course)
            amount = int((course.price - (course.price * coupon.discount * 0.01)) * 100)
        except :
           coupon_code_messege= "coupon code Invalid"


    if amount == 0:
        userCourse = UserCourse(user=user, course=course)
        userCourse.save()
        return redirect('my-courses')
        # enroll direct
    if action == 'create_payment':

        currency = "INR"
        notes = {
            "email": user.email,
            "name": f'{user.first_name} {user.last_name}'
        }
        reciept = f"shreyshukla-{int(time())}"
        order = client.order.create(
            {'receipt': reciept,
             'notes': notes,
             'amount': amount,
             'currency': currency
             }
        )

        payment = Payment()
        payment.user = user
        payment.course = course
        payment.order_id = order.get('id')
        payment.save()

    context = {
        "course": course,
        "order": order,
        "payment": payment,
        "user": user,
        "error": error,
        "coupon": coupon,
        "error": coupon_code_messege,
    }
    return render(request, template_name="courses/check_out.html", context=context)


@csrf_exempt
def verifyPayment(request):
    if request.method == "POST":
        data = request.POST
        context = {}
        print(data)
        try:
            client.utility.verify_payment_signature(data)
            razorpay_order_id = data['razorpay_order_id']
            razorpay_payment_id = data['razorpay_payment_id']

            payment = Payment.objects.get(order_id=razorpay_order_id)
            payment.payment_id = razorpay_payment_id
            payment.status = True

            userCourse = UserCourse(user=payment.user, course=payment.course)
            userCourse.save()

            print("UserCourse",  userCourse.id)

            payment.user_course = userCourse
            payment.save()

            return redirect('my-courses')

        except:
            return HttpResponse("Invalid Payment Details")
        
    return HttpResponse("Invalid Request Method")
