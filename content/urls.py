from django.urls import path
from .views import get_word,generate_content

urlpatterns = [
    path('', get_word, name='get_word'),
    path('generate/', generate_content, name='generate_content'),
]


