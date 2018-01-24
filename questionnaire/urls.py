from django.urls import path
from . import views

urlpatterns = [
    path('',  views.questionnaire, name='questionnaire'),
    path('nextquestion/<id>',  views.next_question, name='next_question'),

]
