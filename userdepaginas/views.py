from django.shortcuts import render

# Create your views here.
def homeuser(request):
    return render(request, 'userdepaginas/homeuser.html')