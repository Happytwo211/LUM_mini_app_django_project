from django.urls import path
from .views import UserBenefitsView, UserList, BenefitsList, ToursList
urlpatterns = [
    path('user/', UserList.as_view(), name='user_list'),
    path('user/<int:pk>/', UserBenefitsView.as_view(), name='user_detail'),
    path('benefits/', BenefitsList.as_view(), name='benefits_list'),
    path('tours_list/', ToursList.as_view(), name='tours_list')
    # path('user/<int:user_id>/<int:data_id>/', UserBenefitsView.as_view(), name='user_detail'),

]