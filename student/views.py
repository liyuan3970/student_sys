from django.shortcuts import render
from .models import Student
# Create your views here.
def index(requset):
    students = Student.objects.all()
    return render(requset,'index.html',context={'students':students})