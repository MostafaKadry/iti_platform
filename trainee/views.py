from django.shortcuts import render, HttpResponse,redirect
from .models import Trainee
data = []
counter = 0
def retrive_trainee(request):
    trainee_data = Trainee.objects.all().values()
    return render(request, 'retrive_trainee.html', {'data': trainee_data})
def add_trainee(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('image')

        print(f"Uploaded file type: {type(uploaded_file)}")
        print(f"Uploaded file : {uploaded_file}")
        Trainee.objects.create(name=request.POST.get('name'), email=request.POST.get('email'), phone=request.POST.get('phone'), address=request.POST.get('address'), image=request.FILES.get('image'))
    return render(request, 'add_trainee.html')

def delete_trainee(request, id):
    if request.method == 'POST':
        trainee_data = Trainee.objects.get(id=id)
        trainee_data.delete()
        return redirect(retrive_trainee)
    return HttpResponse("failed", status=400)

def update_trainee(request, id):
    trainee = Trainee.objects.get(id=id)

    if not trainee:
        return HttpResponse("Trainee not found", status=404)

    if request.method == 'POST':
        trainee.name = request.POST.get('name')
        trainee.email = request.POST.get('email')
        trainee.phone = request.POST.get('phone')
        trainee.address = request.POST.get('address')
        trainee.image = request.FILES.get('image')
        return redirect(retrive_trainee)
    return render(request, 'update_trainee.html', {'trainee': trainee})



