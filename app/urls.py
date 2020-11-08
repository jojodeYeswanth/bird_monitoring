from django.urls import path, re_path
from app import views
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='home'),
    path('user-profile/', views.profile, name="profile"),
    path('bird-profile/', views.birds, name="birds"),

    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout")
]
