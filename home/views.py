from django.shortcuts import render
from .models import Contact, Feature, Portfolio
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
