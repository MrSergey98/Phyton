from django.shortcuts import render, redirect, HttpResponse
from .forms import Lawsuits_datesForm, Responsible_for_lawsuitsForm, LawsuitsForm
from .models import Lawsuits, Lawsuits_dates, Responsible_for_lawsuits
from django.views.generic import UpdateView, DetailView, DeleteView
from django.core.paginator import Paginator
import math

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def table_lawsuits(request):
    table2 = Lawsuits_dates.objects.all()
    count = [i+1 for i in range(math.ceil(table2.count()/5))]
    paginator = Paginator(table2, 5)
    page_number = request.GET.get('page')
    data = paginator.get_page(page_number)
    return render(request, 'main/tables_lawsuits.html', {'lawsuits_dates': data, 'count': count})

def table_responsible(request):
    table1 = Responsible_for_lawsuits.objects.all()
    count = [i+1 for i in range(math.ceil(table1.count()/5))]
    paginator = Paginator(table1, 5)
    page_number = request.GET.get('page')
    data = paginator.get_page(page_number)
    return render(request, 'main/tables_responsible.html', {'responsible_for_lawsuits': data, 'count': count})

def table_responsible_lawsuits(request):
    table3 = Lawsuits.objects.all()
    count = [i+1 for i in range(math.ceil(table3.count()/5))]
    paginator = Paginator(table3, 5)
    page_number = request.GET.get('page')
    data = paginator.get_page(page_number)
    return render(request, 'main/tables_responsible-lawsuits.html', {'lawsuits': data, 'count': count})

def form_lawsuits(request):


    if request.method == 'POST':
        form = Lawsuits_datesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('table_lawsuits')
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
            return redirect('table_responsible_lawsuits')
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
            return redirect('table_responsible')
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
