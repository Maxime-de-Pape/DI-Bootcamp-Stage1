from django.urls import path
from people.views import people_view, person_view

urlpatterns = [
    path('people/', people_view, name='people_view'),
    path('people/<int:id>', person_view, name='person_view'),
]
