from django.shortcuts import render, HttpResponse,redirect


# Create your views here.

data = []
counter = 0
def add_trainee(request):
    global counter
    if request.method == 'POST':
        counter +=1
        trainee_data = {}
        trainee_data['id'] = counter
        trainee_data['name'] = request.POST.get('name')
        trainee_data['email'] = request.POST.get('email')
        trainee_data['phone'] = request.POST.get('phone')
        trainee_data['address'] = request.POST.get('address')
        data.append(trainee_data)
        for d in data:
            print(d)
        return HttpResponse("success")
    return render(request, 'add_trainee.html')

def retrive_trainee(request):
    return render(request, 'retrive_trainee.html', {'data': data})

def delete_trainee(request, id):
    if request.method == 'POST':
        for d in data:
            if d['id'] == id:
                data.remove(d)
                break
        return redirect(retrive_trainee)
    return HttpResponse("failed", status=400)
def update_trainee(request, id):
    trainee = next((d for d in data if d['id'] == id), None)
    print('trainee to update',trainee)
    if not trainee:
        return HttpResponse("Trainee not found", status=404)

    if request.method == 'POST':
        new_trainee_data = {}
        new_trainee_data['name'] = request.POST.get('name')
        new_trainee_data['email'] = request.POST.get('email')
        new_trainee_data['phone'] = request.POST.get('phone')
        new_trainee_data['address'] = request.POST.get('address')
        trainee.update(new_trainee_data)
        print('trainee to update', trainee)
        return redirect(retrive_trainee)

    return render(request, 'update_trainee.html', {'trainee': trainee})



