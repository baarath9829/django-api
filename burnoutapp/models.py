from django.db import models

# Create your models here.
class ChartData(models.Model):
    name = models.CharField(max_length=60)
    amount = models.IntegerField()

    def __str__(self):
        return self.name 

class profileModel(models.Model):
    name = models.CharField(max_length=60,primary_key=True)
    amount = models.IntegerField(default=0)

class chartModel(models.Model):
    name = models.ForeignKey(profileModel,on_delete=models.CASCADE,default=None)
    day = models.IntegerField(default=0)
    expense = models.IntegerField(default=0)
        