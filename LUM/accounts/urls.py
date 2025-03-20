from django.urls import path
from django.urls import include
from .views import SighUpView

urlpatterns = [
    path('signup/',SighUpView.as_view(), name='sighup' )
]