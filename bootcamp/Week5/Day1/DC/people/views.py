from django.shortcuts import render
from .models import Person

def people_view(request):
    people = Person.objects.all().order_by('age')
    context = {'people': people}
    return render(request, 'people.html', context)

def person_view(request, id):
    person = Person.objects.get(id=id)
    context = {'person': person}
    return render(request, 'person.html', context)
