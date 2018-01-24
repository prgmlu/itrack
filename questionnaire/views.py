from django.shortcuts import render
from .models import Question

# Create your views here.
def questionnaire(request):
    question = Question.objects.get(pk = 1)
    return render(request,'questionnaire/index.html',{'question':question})

    
def next_question(request,id):
    if id.isdigit():
        question = Question.objects.get(pk = id)
        return render(request,'questionnaire/index.html',{'question':question})

    else:
        return render(request,'questionnaire/recommended.html',{'recommended':id})
