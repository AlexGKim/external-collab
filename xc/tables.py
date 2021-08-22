import django_tables2 as tables
from django_tables2.utils import A  # alias for Accessor

from .models import Proposal

class ProposalTable(tables.Table):
    proposal = tables.LinkColumn('xc.views.ProposalView',args=[A("proposal")]})
    class Meta:
        model = Proposal
        template_name = "django_tables2/bootstrap.html"
        fields = ("title","collaborators","sponsor","proposal","granted_date","duration","access","active")
