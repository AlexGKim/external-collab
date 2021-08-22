from django.shortcuts import render
from django_tables2 import SingleTableView
from .models import Proposal
from .tables import ProposalTable

def proposal_list(request):
    proposals = Proposal.objects.all()
    return render(request, 'xc/proposal_list.html', {'proposals': proposals})

class ProposalListView(SingleTableView):
    model = Proposal
    table_class = ProposalTable
    template_name = 'xc/proposal.html'
