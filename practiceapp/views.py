from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
# defines function to reutrn httpresonse
def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.is_true = True
    feature1.details = 'Our service is very quick'

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Reliable'
    feature2.is_true = True
    feature2.details = 'Our service is reliable'

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Easy To Use'
    feature3.is_true = False
    feature3.details = 'Our service is easy to use'

    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Affordable'
    feature4.is_true = True
    feature4.details = 'Our service is affordable'

    feature5 = Feature()
    feature5.id = 4
    feature5.name = 'Trustworthy'
    feature5.is_true = True
    feature5.details = 'Our service is trustworthy'

    features = [feature1, feature2, feature3, feature4, feature5] # list of features to be referenced in index.html , see line 100 in index.html file for reference

    for feature in features:
        pass

    return render(request, 'index.html', {'features': features}) # last part references the features list

def counter(request):
    text = request.POST['text'] # uses csrf token 
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})