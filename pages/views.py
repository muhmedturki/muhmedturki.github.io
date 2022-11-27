from django.shortcuts import render
from . models import JoinForm
import os 




# Create your views here.
def index (request):

     number= request.POST.get('number') 
     name= request.POST.get('name')
     phone= request.POST.get('phone')
     image= request.POST.get('image')
     data= JoinForm(number=number, name=name, phone=phone, image=image)
     data.save()
     return render(request,'pages/index.html')

def student (request):
     return render(request,'pages/student.html')
