from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# defines function to reutrn httpresonse
def index(request):
    context = {
        'name': 'Patrick',
        'age': 23,
        'nationality': 'British',
    }
    return render(request, 'index.html', context) #renders index.html file saved in templates folder which is in the root directory, name allows variable to be accessed in html file