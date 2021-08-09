from django.urls import path
from .views import one_subject_quiz

urlpatterns = [
    path('', one_subject_quiz, name='one-sub-quiz')
]
