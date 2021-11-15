from django.urls import path
from . import views
import medicines

urlpatterns = [
    path('', views.index, name='index'),
    path('/medicine/<int:medicineID>/<str:symptomID>', views.map_medicines ),
    path('/medicine', views.medicine)
    ]
