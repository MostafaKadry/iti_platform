from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
database = []
counter = 0
def retrieve_courses(request):
    return render(request, "all_courses.html", {"courses": database})
def add_courses(request):
    global counter
    if request.method == 'POST':
        counter += 1

        course_data = {
            'id' : counter,
            'name': request.POST.get('name'),
            'track': request.POST.get('track'),
            'hours': request.POST.get('hours')
        }
        database.append(course_data)
        return redirect(add_courses)
    return render(request, 'course_form.html')
def delete_courses(request, id):

    if request.method == 'POST':
        for data in database:
            if data['id'] == id:
                database.remove(data)
                break
        return redirect(retrieve_courses)
    return HttpResponse("failed", status=400)
def update_courses(request, id):
    course = next((c for c in database if c['id'] == id), None)

    if not course:
        return HttpResponse("Trainee not found", status=404)

    if request.method == 'POST':
        new_course_data = {}
        new_course_data['name'] = request.POST.get('name')
        new_course_data['email'] = request.POST.get('email')
        new_course_data['phone'] = request.POST.get('phone')
        new_course_data['address'] = request.POST.get('address')
        course.update(new_course_data)

        return redirect(retrieve_courses)

    return render(request, 'update_course.html', {'course': course})