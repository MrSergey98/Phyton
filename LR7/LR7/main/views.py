from django.shortcuts import render, redirect, HttpResponse
from .forms import Lawsuits_datesForm, Responsible_for_lawsuitsForm, LawsuitsForm
from .models import Lawsuits, Lawsuits_dates, Responsible_for_lawsuits

# Create your views here.

def index(request):
    
    form1 = Lawsuits_datesForm()
    form2 = LawsuitsForm()
    form3 = Responsible_for_lawsuitsForm()
    data = {
        'form1': form1,
        'form2': form2,
        'form3': form3,
    }
    return render(request, 'main/index.html', data)

def tables(request):
    table1 = Responsible_for_lawsuits.objects.all()
    table2 = Lawsuits_dates.objects.all()
    table3 = Lawsuits.objects.all()
    return render(request, 'main/tables.html', {'responsible_for_lawsuits': table1, 'lawsuits_dates': table2, 'lawsuits': table3})

def form_lawsuits(request):
    if request.method == 'POST':
        form = Lawsuits_datesForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('home')

def form_responsible_for_lawsuits(request):
    if request.method == 'POST':
        responsible=Responsible_for_lawsuits.objects.get(name=request.POST['responsible'])
        lawsuit = Lawsuits_dates.objects.get(pk=request.POST['lawsuit'])
        form = LawsuitsForm({'responsible': responsible , 'lawsuit': lawsuit})
        if form.is_valid():
            form.save()
        return redirect('home')

def form_responsible(request):
    if request.method == 'POST':
        form = Responsible_for_lawsuitsForm(request.POST)
        if form.is_valid():
            form.save()

    return redirect('home')


