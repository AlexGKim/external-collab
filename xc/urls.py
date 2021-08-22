from django.urls import path
from . import views

urlpatterns = [
   path('', views.ProposalListView.as_view(), name='proposal_list'),
#    path('', views.proposal_list, name='proposal_list'),
]
