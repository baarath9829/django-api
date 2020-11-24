from django.contrib import admin
from .models import ChartData, chartModel, profileModel
# Register your models here.
admin.site.register(ChartData)
admin.site.register(chartModel)
admin.site.register(profileModel)