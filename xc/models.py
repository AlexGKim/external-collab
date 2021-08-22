from django.conf import settings
from django.db import models
from django.core.validators import validate_comma_separated_integer_list
# from django_postgres_extensions.models.fields import ArrayField
from django.utils import timezone

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    institution = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Proposal(models.Model):
    sponsor = models.ForeignKey(Person, on_delete=models.CASCADE)
    collaborators =  models.ManyToManyField('Person', related_name='proposals')
    title = models.CharField(max_length=200)
    proposal = models.URLField(null=True, blank=True)
    project = models.CharField(validators=[validate_comma_separated_integer_list], max_length=20) 
    granted_date = models.DateField(default=timezone.now)
    duration = models.CharField(max_length=400,null=True, blank=True)
    access = models.CharField(max_length=400,null=True, blank=True)
    active = models.BooleanField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
