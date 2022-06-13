from . import views
from django.urls import path

urlpatterns = [
    path('create/', views.PostCreate.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
]