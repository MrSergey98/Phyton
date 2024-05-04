from .models import Lawsuits_dates, Responsible_for_lawsuits, Lawsuits
from django.forms import ModelForm, DateTimeInput, TextInput

class Lawsuits_datesForm(ModelForm):
    class Meta:
        model = Lawsuits_dates
        fields = ['date', 'info']
        widgets = {
            "date": DateTimeInput(attrs={
                "name":"date",
                'class': 'form-control',
                'type': "date"
            }),
            "info": TextInput(attrs={
                "name":"info",
                'class': 'form-control',
                'type': "text"})
        }

class LawsuitsForm(ModelForm):
    class Meta:
        model = Lawsuits
        fields = ['responsible', 'lawsuit', 'info']
        widgets = {
            'responsible': TextInput(attrs={
                "name":"responsible",
                'class': 'form-control',
                'type': 'text'
            }),
            'lawsuit': TextInput(attrs={
                "name":"id",
                'class': 'form-control',
                'type': 'text'
            }),
            "info": TextInput(attrs={
                "name":"info",
                'class': 'form-control',
                'type': "text"})
        }

class Responsible_for_lawsuitsForm(ModelForm):
    class Meta:
        model = Responsible_for_lawsuits
        fields = ['name', "info"]
        widgets = {
            'name': TextInput(attrs={
                "name":"name",
                'class': 'form-control',
                'type': 'text'
            }),
            "info": TextInput(attrs={
                "name":"info",
                'class': 'form-control',
                'type': "text"})
        }


