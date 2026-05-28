from django.urls import path
from sss import views

urlpatterns = [
    path('', views.sss, name='sss_home'),
]