from django.http.response import HttpResponse
from django.shortcuts import render
import json
import os

# Create your views here.
from questions.models import QuesMcq

def one_subject_quiz(request):
    question_list = []
    subject = "physics"
    no_of_ques = 30
    time = 30
    
    ques_objs = QuesMcq.objects.filter(subject=subject)
    for ques in ques_objs:
        a = {
            'question' : ques.question,
            'option_1' : ques.option_1,
            'option_2' : ques.option_2,
            'option_3' : ques.option_3,
            'option_4' : ques.option_4,
            'answer' : ques.answer
        }
        question_list.append(a)
        
    json_object = json.dumps(question_list, indent = 4)
    with open("static/json/fate.json", "w") as outfile:
        outfile.write(json_object)
    
    return render(request, 'quiz.html', {'question_list' : json.dumps(question_list)})
