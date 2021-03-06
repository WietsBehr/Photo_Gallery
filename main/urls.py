from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path('', views.login, name="login"),
    path('login/', views.login, name="login"),
    path('test/', views.test, name="test"),
    path('register/', views.register, name="register"),
    path('gallery/', views.gallery, name="gallery"),
    path('upload/<int:user_id>/', views.upload, name="upload"),
]