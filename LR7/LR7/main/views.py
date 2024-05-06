from django.shortcuts import render, redirect, HttpResponse
from .forms import Lawsuits_datesForm, Responsible_for_lawsuitsForm, LawsuitsForm
from .models import Lawsuits, Lawsuits_dates, Responsible_for_lawsuits
from django.views.generic import UpdateView, DetailView, DeleteView

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def table_lawsuits(request):
    table2 = Lawsuits_dates.objects.all()
    return render(request, 'main/tables_lawsuits.html', {'lawsuits_dates': table2})

def table_responsible(request):
    table1 = Responsible_for_lawsuits.objects.all()
    return render(request, 'main/tables_responsible.html', {'responsible_for_lawsuits': table1})

def table_responsible_lawsuits(request):
    table3 = Lawsuits.objects.all()
    return render(request, 'main/tables_responsible-lawsuits.html', {'lawsuits': table3})

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
    else:
        form = Lawsuits_datesForm()
        data = {
        'form': form
        }
        return render(request, 'main/lawsuit.html', data)

def form_responsible_for_lawsuits(request):
    if request.method == 'POST':
        responsible=Responsible_for_lawsuits.objects.get(name=request.POST['responsible'])
        lawsuit = Lawsuits_dates.objects.get(pk=request.POST['lawsuit'])
        form = LawsuitsForm({'responsible': responsible , 'lawsuit': lawsuit, 'info': request.POST['info']})
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LawsuitsForm()
        data = {
            "form": form
        }
        return render(request, 'main/responsible_lawsuit.html', data)

def form_responsible(request):
    if request.method == 'POST':
        form = Responsible_for_lawsuitsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Responsible_for_lawsuitsForm()
        data = {
            'form': form
        }
        return render(request, 'main/responsible.html', data)


class DetailViewLawsuit(DetailView):
    model = Lawsuits_dates
    template_name = "main/lawsuit-detail.html"
    context_object_name = 'lawsuit'

class DetailViewResponsible(DetailView):
    model = Responsible_for_lawsuits
    template_name = "main/responsible-detail.html"
    context_object_name = 'responsible'

class DetailViewResponsible_lawsuit(DetailView):
    model = Lawsuits
    template_name = "main/responsible_lawsuit-detail.html"
    context_object_name = 'responsible_lawsuit'

class UpdateLawsuit(UpdateView):
    model=Lawsuits_dates
    template_name = 'main/lawsuit.html'
    form_class = Lawsuits_datesForm

class UpdateResponsible(UpdateView):
    model=Responsible_for_lawsuits
    template_name = 'main/responsible.html'
    form_class = Responsible_for_lawsuitsForm

class UpdateResponsible_Lawsuit(UpdateView):
    model=Lawsuits
    template_name = 'main/responsible_lawsuit.html'
    form_class = LawsuitsForm

class DeleteLawsuit(DeleteView):
    model=Lawsuits_dates
    template_name = 'main/delete.html'
    success_url = '/'

class DeleteResponsible(DeleteView):
    model=Responsible_for_lawsuits
    template_name = 'main/delete.html'
    success_url = '/'

class DeleteResponsible_Lawsuit(DeleteView):
    model=Lawsuits
    template_name = 'main/delete.html'
    success_url = '/'
