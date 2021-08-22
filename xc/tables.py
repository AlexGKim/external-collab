import django_tables2 as tables
from django_tables2.utils import A  # alias for Accessor

from .models import Proposal

class CustomTextLinkColumn(tables.LinkColumn):

   def __init__(self, viewname, urlconf=None, args=None, 
     kwargs=None, current_app=None, attrs=None, custom_text=None, **extra):
     super(CustomTextLinkColumn, self).__init__(viewname, urlconf=urlconf, 
     args=args, kwargs=kwargs, current_app=current_app, attrs=attrs, **extra)

     self.custom_text = custom_text

     def render(self, value, record, bound_column):
       return super(CustomTextLinkColumn, self).render(self,
         self.custom_text if self.custom_text else value,
         record, bound_column)

class ProposalTable(tables.Table):
#     proposal = CustomTextLinkColumn('xc.views.ProposalListView.as_view()',args=[A("proposal")], custom_text='proposal', verbose_name='Proposal',)

    class Meta:
        model = Proposal
        template_name = "django_tables2/bootstrap.html"
        fields = ("title","collaborators","sponsor","granted_date","duration","access","active","proposal")
