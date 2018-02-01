from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Question


# Create your views here.
register_form = UserCreationForm()
login_form = AuthenticationForm()
context = {
    'register_form': register_form,
    'login_form': login_form
    }
def questionnaire(request):
    return render(request, 'questionnaire/index.html', context)


def view_questions(request):
    question = Question.objects.get(pk=1)
    global context
    context.update({'question':question})
    return render(request, 'questionnaire/questions.html', context)


def next_question(request):
    id = request.GET['answer']
    if id.isdigit():
        question = Question.objects.get(pk=id)
        return render(request, 'questionnaire/questions.html', {'question': question, 'register_form': register_form,
                                                                'login_form': login_form})

    else:
        return render(request, 'questionnaire/recommended.html', {'recommended': id, 'register_form': register_form,
                                                                  'login_form': login_form})
