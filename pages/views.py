from django.http import HttpResponse

def homePageView(request):
    return HttpResponse("<h1><b>Hello, world!</b></h1>")
