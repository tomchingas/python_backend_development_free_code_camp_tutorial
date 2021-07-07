from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# defines function to reutrn httpresonse
def index(request):
    return render(request, 'index.html') #renders index.html file saved in templates folder which is in the root directory, name allows variable to be accessed in html file

def counter(request):
    text = request.POST['text'] # uses csrf token 
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})