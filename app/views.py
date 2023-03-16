from django.shortcuts import render

# Create your views here.
def ifelif(request):
    d={'a':100,'b':150,'c':200}
    return render(request,'ifelif.html',d)
