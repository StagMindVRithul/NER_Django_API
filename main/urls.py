from django.urls import path 
from . import views 
from .views import LoginAPI, RegisterAPI, CreateMedicalView



urlpatterns = [
    path("",views.home,name='home'),
    path("home",views.home,name='home'),
    path("sign-up",views.sign_up,name='sign_up'),
    path("create-medical",views.create_medical,name='create_medical'),
    path("api/register/",RegisterAPI.as_view(),name='register'),
    path("api/login/",LoginAPI.as_view(),name='login'),
    path('api/create-medical/', CreateMedicalView.as_view(), name='create-medical-api'),
]
