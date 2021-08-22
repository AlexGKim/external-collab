from django.urls import path
from . import views

urlpatterns = [
    path('', views.proposal_list, name='proposal_list'),
]
