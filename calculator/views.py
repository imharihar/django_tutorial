from django.shortcuts import render

# Create your views here.
def calcy(request):
    return render(request,'calculator/calcy.html',{})