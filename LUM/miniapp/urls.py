from django.urls import path
from .views import UserBenefitsView, UserList, BenefitsList

urlpatterns = [
    path('user/', UserList.as_view(), name='user_list'),
    path('user/<int:pk>/', UserBenefitsView.as_view(), name='user_detail'),
    path('benefits/', BenefitsList.as_view(), name='benefits_list')
]