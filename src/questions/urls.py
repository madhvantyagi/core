from django.urls import path
from .views import index_questions

urlpatterns = [
    path('', index_questions, name='index-page'),
]
