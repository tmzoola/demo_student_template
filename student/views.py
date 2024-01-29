from django.shortcuts import render

# Create your views here.


def index(request):
    data = {
        'title':'Student Management'
    }
    
    return render(request, 'student/index.html', context=data)