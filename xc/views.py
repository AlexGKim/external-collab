from django.shortcuts import render
from .models import Proposal

def proposal_list(request):
    proposals = Proposal.objects.all()
    return render(request, 'xc/proposal_list.html', {'proposals': proposals})
