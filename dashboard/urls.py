from django.urls import path 

from .views import *

app_name="dashboard"

urlpatterns=[
    path("",DashBoardView.as_view(),name="dashboard"),
    path("settings/",SettingsView.as_view(),name="settings")
]
