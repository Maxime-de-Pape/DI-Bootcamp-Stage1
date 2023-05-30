from django.urls import path
from info.views import family_view, animal_view

urlpatterns = [
    path('family/<int:family_id>', family_view, name='family_view'),
    path('animal/<int:animal_id>', animal_view, name='animal_view'),
]
