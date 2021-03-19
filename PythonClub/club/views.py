from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def resources(request):
    resourceName = Resource.objects.all()
    return render(request, 'club/resources.html', {'resourceName': resourceName})