from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello!")
# Create your views here.
def hello_there(request):
    return render(
        request,
        'testApp/index.html',
        {
            'title': 'test',
        }
    )