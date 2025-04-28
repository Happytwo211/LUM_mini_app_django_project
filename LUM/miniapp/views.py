from django.shortcuts import render
from .models import User_benefits_data, User, Benefits, Tours
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class UserBenefitsView(LoginRequiredMixin,DetailView):
    raise_exception = True
    model = User_benefits_data
    ordering = 'user'
    template_name = 'user_benefits_data.html'
    context_object_name = 'user_benefits_data'


class UserList(LoginRequiredMixin,ListView):

    raise_exception = True
    model = User
    template_name = 'user_list.html'
    context_object_name = 'user_list'


class BenefitsList(LoginRequiredMixin,ListView):
    raise_exception = True
    model = Benefits
    template_name = 'benefits.html'
    context_object_name = 'benefits_list'

class ToursList(ListView):

    # raise_exception = True
    model = Tours
    template_name = 'tours_list.html'
    context_object_name = 'tours_list'

