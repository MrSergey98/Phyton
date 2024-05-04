from django.contrib import admin
from .models import Lawsuits, Responsible_for_lawsuits, Lawsuits_dates
admin.site.register(Lawsuits)
admin.site.register(Responsible_for_lawsuits)
admin.site.register(Lawsuits_dates)

# Register your models here.
