from django.shortcuts import render

# Create your views here.
def sample(request):
    d={'name':'ASHISH','age':'23'}
    return render(request,'file.html',context=d)