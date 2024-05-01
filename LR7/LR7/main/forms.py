from .models import Lawsuits_dates, Responsible_for_lawsuits, Lawsuits
from django.forms import ModelForm, DateTimeInput, TextInput

class Lawsuits_datesForm(ModelForm):
    class Meta:
        model = Lawsuits_dates
        fields = ['date']
        widgets = {
            "date": DateTimeInput(attrs={
                "name":"date",
                'class': 'form-control',
                'type': "date"
            })
        }

class LawsuitsForm(ModelForm):
    class Meta:
        model = Lawsuits
        fields = ['responsible', 'lawsuit']
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
            })
        }

class Responsible_for_lawsuitsForm(ModelForm):
    class Meta:
        model = Responsible_for_lawsuits
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={
                "name":"name",
                'class': 'form-control',
                'type': 'text'
            })
        }


