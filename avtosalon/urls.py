from django.urls import path, re_path
from . import views
urlpatterns = [
    path('index/', views.index, name='index'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]