from django.shortcuts import render
# Create your views here.
#from django.template import RequestContext

def index(request):
    #RequestContext(request)
    return render(request,'main/index.html')
