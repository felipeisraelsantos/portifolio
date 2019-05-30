from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]