from django.db import models

# Create your models here.
class Responsible_for_lawsuits(models.Model):

    name = models.CharField(max_length=80)
    info = models.TextField(null=True)
    def __str__(self) -> str:
        return self.name
    def get_absolute_url(self):
        return f'/responsible/{self.id}'
    

class Lawsuits_dates(models.Model):

    date = models.DateField()
    info = models.TextField(null=True)
    def get_absolute_url(self):
        return f'/lawsuit/{self.id}'
    def __str__(self) -> str:
        return str(self.id)


class Lawsuits(models.Model):

    responsible = models.ForeignKey('Responsible_for_lawsuits', on_delete=models.PROTECT)
    lawsuit = models.ForeignKey('Lawsuits_dates', on_delete=models.PROTECT)
    info = models.TextField(null=True)
    def get_absolute_url(self):
        return f'/responsible-lawsuit/{self.id}'
    def __str__(self):
        return str(self.id)

