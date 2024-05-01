from django.db import models

# Create your models here.
class Responsible_for_lawsuits(models.Model):

    name = models.CharField(max_length=80)

    def __str__(self) -> str:
        return self.name


class Lawsuits_dates(models.Model):

    date = models.DateTimeField()

    def __str__(self) -> str:
        return self.date


class Lawsuits(models.Model):

    responsible = models.ForeignKey('Responsible_for_lawsuits', on_delete=models.PROTECT)
    lawsuit = models.ForeignKey('Lawsuits_dates', on_delete=models.PROTECT)

