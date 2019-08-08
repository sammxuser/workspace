from django.urls import path
from . import views

urlpatterns = [
#/workspace_app/
    path('', views.index, name = 'index'),
#e.g /workspace_app/task_number/
    path('<task_number>/', views.task_detail, name = 'detail'),
]
