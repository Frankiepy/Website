from django.conf.urls import url
from django.urls import path, include
from . import views
from . import models

app_name = 'match'

urlpatterns = [
    path('', views.match, name="list"),
    url('create/', views.profile_create, name="create"),
    path('<slug:slug>/', views.match_detail, name="detail"),
]