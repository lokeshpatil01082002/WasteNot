from django.shortcuts import render

# Create your views here.
def LandingPage(request):
    return render (request,'landing.html')

def LoginPage(request):
    return render (request,'login.html')
def SignupPage(request):
    return render (request,'signup.html')