from django.urls import path
from .views import one_subject_quiz, page_view

urlpatterns = [
    path('', one_subject_quiz, name='one-sub-quiz'),
    path('1/', page_view),
]
