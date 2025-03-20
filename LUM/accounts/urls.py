from django.urls import path
from django.urls import include
from .views import SignUpView

urlpatterns = [
    path('signup/',SignUpView.as_view(), name='sighup' )
]