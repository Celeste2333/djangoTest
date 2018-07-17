from django.shortcuts import render

# Create your views here.


def getstart(request):
    return render(request, 'start.html')