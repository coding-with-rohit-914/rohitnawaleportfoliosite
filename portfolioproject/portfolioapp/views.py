from django.shortcuts import render, redirect
from .models import FeedbackData

def RohitPage(request):
    return render(request, 'RohitPage.html')

def index(request):
    return render(request, 'index.html')

def contactPage(request):
    return render(request, 'contactPage.html')

def AboutPage(request):
    return render(request, 'AboutPage.html')

def MyWorkPage(request):
    return render(request, 'MyWorkPage.html')

def ServicesPage(request):
    return render(request, 'ServicesPage.html')

def ContactPage(request):
    return render(request, 'contactPage.html')

def Feedback(request):
    if request.method == 'GET':
        return render(request, 'Feedback.html')
    else:
        FeedbackData(
        name = request.POST.get('Name'),
        email = request.POST.get('Email'),
        feedback = request.POST.get('feedback')
        ).save()
        return redirect('Feedback')
