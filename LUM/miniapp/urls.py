from django.urls import path
from .views import UserBenefitsView, UserList

urlpatterns = [
    path('user/', UserList.as_view(), name='user_list'),
    path('user/<int:pk>/', UserBenefitsView.as_view(), name='user_detail'),

]