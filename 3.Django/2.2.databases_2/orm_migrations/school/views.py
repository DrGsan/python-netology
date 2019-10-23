from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'

    context = {}
    ordering = 'group'
    students = Student.objects.order_by(ordering).prefetch_related('teacher')
    context['object_list'] = students

    return render(request, template, context)