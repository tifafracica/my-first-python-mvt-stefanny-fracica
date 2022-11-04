from django.http import HttpResponse
from django.shortcuts import render

def relatives(request):
    return render(request, 'relatives.html')