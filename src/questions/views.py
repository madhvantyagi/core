from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import QuesIntType, QuesMcq
import json

# Create your views here.
def index_view(request):
    questions_mcq = QuesMcq.objects.all()
    questions_int_type = QuesIntType.objects.all()
    
    question_list = []
    for ques in questions_mcq:
        a = {
            'question' : ques.question,
            'option_1' : ques.option_1,
            'option_2' : ques.option_2,
            'option_3' : ques.option_3,
            'option_4' : ques.option_4,
            'answer' : ques.answer
        }
        question_list.append(a)
        # print(question_list)
    
    return render(request, 'quiz.html', {'question_list' : json.dumps(question_list)})