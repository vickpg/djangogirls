from django.urls import path
from . import views

Post.objects.get(pk=pk)

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]