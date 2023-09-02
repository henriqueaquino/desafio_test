from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('empregados/', views.EmpregadoList.as_view()),
    path('departamentos/', views.DepartamentoList.as_view()),
    path('empregados/<int:pk>/', views.EmpregadoDetail.as_view()),
    path('departamentos/<int:pk>/', views.DepartamentoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)