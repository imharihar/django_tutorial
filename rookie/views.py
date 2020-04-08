from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    context = {}
    day = datetime.date.today()
    context['day'] = day
    return render(request,'rookie/index.html',context)
