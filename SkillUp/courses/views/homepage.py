from courses.models import course
from django.views.generic import ListView


class HomePageView(ListView):
    template_name = "courses/home.html"
    queryset = course.Course.objects.filter(active=True)
    context_object_name = 'courses'
