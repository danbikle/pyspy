from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'pyspy/index.html', context)
