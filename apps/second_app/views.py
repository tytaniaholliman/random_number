from django.shortcuts import render
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    word= get_random_string(length=14)
    if 'counter' not in request.session:
        request.session['counter'] = 1
    request.session['counter'] += 1
    context = {
        'word': word,
        'counter': request.session['counter']
    }
    return render(request,'second_app/index.html', context)

def generate(request):
    return redirect('/')

def reset (request):
    request.session['counter'] = 0
    return redirect('/')