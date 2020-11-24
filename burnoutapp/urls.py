from django.urls import path
from .views import ChartDataView, profile, test, chartdata, chart


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns =[
    path('chartdata',ChartDataView,name='ChartDataView'),
    path('chartdata/<int:id>',chartdata,name='Profile'),
    path('test',test,name='test'),
    path('profile',profile,name="profile"),
    path('chart',chart,name='chart'),
]
