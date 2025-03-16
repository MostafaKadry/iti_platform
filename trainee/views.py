from django.contrib.auth.views import LoginView
from django.shortcuts import render, HttpResponse,redirect, get_object_or_404

from .login_trainee_form import LoginForm
from .models import Trainee
from course.models import Course
import os
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View

from django.contrib.auth import authenticate, login, logout

class TrainerListView(ListView):
    model = Trainee
    template_name = 'retrive_trainee.html'
    context_object_name = 'data'

# def retrive_trainee(request):
#     trainee_data = Trainee.objects.all()
#     return render(request, 'retrive_trainee.html', {'data': trainee_data})

# Class Based View
class TraineeCreateView(View):
    template_name = 'add_trainee.html'
    success_url = reverse_lazy('get_trainee')

    def get(self, request):
        courses = Course.get_all_courses()
        return render(request, self.template_name, {"courses": courses})

    def post(self, request, *args, **kwargs):
        enrolled_course_id = request.POST.get("course")

        if enrolled_course_id:
            enrolled_course = Course.get_course_by_id(enrolled_course_id)
            Trainee.add_trainee(name=request.POST.get('name'), email=request.POST.get('email'), password=request.POST.get('password'),phone=request.POST.get('phone'), address=request.POST.get('address'), image=request.FILES.get('image'), course=enrolled_course)
            return redirect(self.success_url)

# def add_trainee(request):
#     courses = Course.get_all_courses()
#     if request.method == 'POST':
#         enrolled_course_id = request.POST.get("course")
#         if enrolled_course_id:
#             enrolled_course = Course.get_course_by_id(enrolled_course_id)
#             Trainee.add_trainee(name=request.POST.get('name'),email=request.POST.get('email'), phone=request.POST.get('phone'), address=request.POST.get('address'), image=request.FILES.get('image'), course=enrolled_course)
#
#     return render(request, 'add_trainee.html', {"courses": courses})


# Generic view
class TraineeDeleteView(DeleteView):
    model = Trainee
    success_url = reverse_lazy('get_trainee')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        old_image_path = self.object.image.path
        if os.path.exists(old_image_path):
            os.remove(old_image_path)

        return super().post(request, *args, **kwargs)


# def delete_trainee(request, id):
#     if request.method == 'POST':
#         trainee_data = Trainee.objects.get(id=id)
#         old_image_path = os.path.join(trainee_data.image.path)
#         if os.path.exists(old_image_path):
#             os.remove(old_image_path)
#         trainee_data.delete()
#         return redirect('get_trainee')
#     return HttpResponse("failed", status=400)

class TraneeUpdateView(UpdateView):
    model = Trainee
    success_url = reverse_lazy('get_trainee')
    template_name = 'update_trainee.html'

    def get(self, request, id):
        trainee = get_object_or_404(Trainee, id=id)
        return render(request, self.template_name, {'trainee': trainee})

    def post(self, request, id):
        trainee = get_object_or_404(Trainee, id=id)

        trainee.name = request.POST.get('name')
        trainee.email = request.POST.get('email')
        trainee.phone = request.POST.get('phone')
        trainee.address = request.POST.get('address')

        if 'image' in request.FILES:
            if trainee.image and os.path.exists(trainee.image.path):
                os.remove(trainee.image.path)
            trainee.image = request.FILES.get('image')

        trainee.save()
        return redirect(self.success_url)


# def update_trainee(request, id):
#     trainee = get_object_or_404(Trainee, id=id)
#
#     if not trainee:
#         return HttpResponse("Trainee not found", status=404)
#
#     if request.method == 'POST':
#         trainee.name = request.POST.get('name')
#         trainee.email = request.POST.get('email')
#         trainee.phone = request.POST.get('phone')
#         trainee.address = request.POST.get('address')
#         trainee.image = request.FILES.get('image')
#
#     return render(request, 'update_trainee.html', {'trainee': trainee})


class TraineeLoginView(View):
    def get(self, request):
        context = {"form": LoginForm()}
        return render(request, 'login_trainee.html', context)

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            logged_user = Trainee.objects.get(email=email)
        except Trainee.DoesNotExist:
            return HttpResponse("Trainee not found", status=401)

        if logged_user.check_password(password):
            request.session['logged_user'] = logged_user.id
            return redirect('get_trainee')
        else:
            return HttpResponse("Invalid password", status=401)