from django.urls import path
from .views import UserBenefitsView

urlpatterns = [
    path('user/<int:pk>/', UserBenefitsView.as_view(), name = 'user_benefits')
]