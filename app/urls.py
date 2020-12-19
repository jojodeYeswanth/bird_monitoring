from django.urls import path, re_path
from app import views
from django.conf.urls import url
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='home'),
    path('user-profile/', views.profile, name="profile"),
    url(r'^add/cage/$', views.AddCage, name='add-cage'),
    url(r'^add/bird/$', views.AddBird, name='add-bird'),
    path('select-option/', views.cageoption.as_view(), name='cageoption'),
    url(r'^bird-profile/$', views.BirdProfileView.as_view(), name='birds'),

    url(r'^/(?P<stream_path>(.*?))/$', views.dynamic_stream, name="videostream"),
    url(r'^detect-video/$', views.indexscreen, name='detect_video'),

    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout")
]
