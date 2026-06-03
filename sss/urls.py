from django.urls import path
from sss import views

urlpatterns = [
    path('', views.sss, name='sss_home'),
    path('<int:chai_id>/', views.chai_detail, name='chai_detail'),
    path('chai_stores/', views.chai_store_view, name='chai_stores'),
]