from django.shortcuts import render, redirect
from .models import Contact, Feature, Portfolio, Subscribe
from django.contrib import messages
import json
from django.http import JsonResponse
# Create your views here.


def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

    # Feature
    queryset = Feature.objects.all()

    # Portfolio
    queryset2 = Portfolio.objects.all()

    context = {
        'queryset': queryset,
        'queryset2': queryset2,
    }

    return render(request, 'index.html', context)

def subscribe(request):
    if request.method == "POST":
        email = request.POST['sub_email']

        obj = Subscribe(email=email)
        obj.save()
        messages.success(request, "Your email has been sucessfully ragister.")
        return redirect('home')
    else:
        return redirect('home')

def subscribe_validation(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data['emailid']

        if Subscribe.objects.filter(email=email).exists():
            return JsonResponse({'email_error':'This email already ragister, try another one'}, status=409)

        return JsonResponse({'email_valid':True})