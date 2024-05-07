from django.contrib import admin
from .models import Lawsuits, Responsible_for_lawsuits, Lawsuits_dates

class LawsuitsAdmin(admin.ModelAdmin):
    list_display = ("id", "responsible", "lawsuit")

class Responsible_for_lawsuitsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "info")

class Lawsuits_datesAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "info")

admin.site.register(Lawsuits, LawsuitsAdmin)
admin.site.register(Responsible_for_lawsuits, Responsible_for_lawsuitsAdmin)
admin.site.register(Lawsuits_dates, Lawsuits_datesAdmin)

# Register your models here.
