from django.shortcuts import render, redirect, HttpResponse
from .models import Course
from course.model_form import CourseForm
# Create your views here.

def retrieve_courses(request):
    c_data = Course.objects.all().values()
    return render(request, "all_courses.html", {"courses": c_data})
def add_courses(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(add_courses)
    else:
        return render(request, 'course_form.html', {'CourseForm': CourseForm()})
def delete_courses(request, id):
    if request.method == 'POST':
        course = Course.objects.get(id=id)
        course.delete()
        return redirect(retrieve_courses)
    return HttpResponse("failed", status=400)

def update_courses(request, id):
    course = Course.get_course_by_id(id)

    if not course:
        return HttpResponse("Trainee not found", status=404)

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect(retrieve_courses)
    old_course = CourseForm(instance=course)
    return render(request, 'update_course.html', {'course': old_course})


