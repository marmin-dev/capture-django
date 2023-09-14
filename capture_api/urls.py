from django.urls import path
from . import views

urlpatterns = [
    path('',views.capture_one),
    path("list/",views.capture_list)

]
