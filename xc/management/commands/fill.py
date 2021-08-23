from django.core.management.base import BaseCommand, CommandError
from xc.models import Person, Project, Proposal






class Command(BaseCommand):
    help = 'Fills with initial data'


    def handle(self, *args, **options):

        people=[ \
            {"first_name": "Alex", \
            "last_name": "Kim", \
            "institution": "Lawrence Berkeley National Laboratory", \
            "email": "agkim@lbl.gov"},
            {"first_name": "David", \
            "last_name": "Cinabro", \
            "institution": "Wayne State University", \
            "email": "david.cinabro@wayne.edu"},
            {"first_name": "David", \
            "last_name": "Moutard", \
            "institution": "Wayne State University", \
            "email": "david.moutard@wayne.edu"},
             {"first_name" :"Robert", \
            "last_name": "Carr", \
            "institution": "Wayne State University", \
            "email" :"robert.s.carr@wayne.edu"}, \
            {"first_name" :"David", \
            "last_name": "Alonso", \
            "institution": "Oxford University", \
            "email" :"david.alonso@physics.ox.ac.uk"}, \
            {"first_name" :"Andreu", \
            "last_name": "Font-Ribera", \
            "institution": "Institut de Física d’Altes Energies ", \
            "email" :"afont@ifae.es"}, \
            ]

        for person in people:
            try:
                Person.objects.create(**person)
            except:
                pass

        projects = [ \
            {"title": "Automatic Detection and Classification of Transients in DESI Galaxy Spectra", \
            "url": "https://desi.lbl.gov/desipub/app/PB/show_project?pid=19", 
            "id": 19},
            {"title": "A search for TDE host galaxies with extreme coronal emission lines with DESI", \
            "url": "https://desi.lbl.gov/desipub/app/PB/show_project?pid=75", 
            "id": 75},
            {"title": "London Mocks", \
            "url": "https://desi.lbl.gov/desipub/app/PB/show_project?pid=15", 
            "id": 15},
            ]

        for project in projects:
            try:
                Project.objects.create(**project)
            except:
                pass

        proposal= {"id":4, "sponsor": Person.objects.get(first_name='Alex',last_name='Kim'), \
            "title": "Zowada Follow-up of DESI Discoveries",
            "proposal": "https://desi.lbl.gov/trac/attachment/wiki/ExternalCollaborationCommittee/Wayne_State_DESI_XC-2.pdf",
            "granted_date": "2021-02-01",
            "duration": "SV",
            "access": "Slack, DESI Transient Outputs",
            "active": True}

        try:
            p1 = Proposal.objects.create(**proposal)
            p1.project.add(Project.objects.get(id=19))
            p1.project.add(Project.objects.get(id=75))
            p1.collaborators.add(Person.objects.get(first_name='David',last_name='Cinabro'))
            p1.collaborators.add(Person.objects.get(first_name='David',last_name='Moutard'))
            p1.collaborators.add(Person.objects.get(first_name='Robert',last_name='Carr'))
        except:
            pass

        proposal= {"id":1, "sponsor": Person.objects.get(first_name='Andreu',last_name='Font-Ribera'), \
            "title": "London Mocks",
            "granted_date": "2019-06-19",
            "duration": "1 year",
            "active": False}


        try:
            p1 = Proposal.objects.create(**proposal)
            p1.project.add(Project.objects.get(id=15))
            p1.collaborators.add(Person.objects.get(first_name='David',last_name='Alonso'))
        except:
            pass


