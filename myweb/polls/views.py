from django.http import HttpResponse
def index(resquest):
    return HttpResponse("Hello World, You're at the polls index")
# Create your views here.
