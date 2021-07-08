from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
# defines function to reutrn httpresonse
def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features}) # last part references the features list

def counter(request):
    text = request.POST['text'] # uses csrf token 
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})