from django.shortcuts import render
from .models import PersonelInfo
from django.shortcuts import redirect
def index(request):
    infos = PersonelInfo.objects.all()
    return render(request, 'index.html', {'infos':infos})
def delete(request, id):
    info = PersonelInfo.objects.get(pk=id)
    info.delete()
    return redirect('/')
def add_info(request):
    return render(request, 'add_info.html')

def create(request):
    print(request.POST)
    name = request.GET['name']
    appoinment = request.GET['appoinment']
    joining_date = request.GET['joining_date']
    personel_info = PersonelInfo(name=name, appoinment=appoinment, joining_date=joining_date)
    personel_info.save()
    return redirect('/')
def edit(request, id):
    infos = PersonelInfo.objects.get(pk=id)
    context = {
        'infos': infos
    }
    return render(request, 'edit_info.html', context)

def update(request, id):
    infos = PersonelInfo.objects.get(pk=id)
    infos.name = request.GET['name']
    infos.appoinment = request.GET['appoinment']
    infos.joining_date = request.GET['joining_date']
    infos.save()
    return redirect('/')
