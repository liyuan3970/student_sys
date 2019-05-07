from django.shortcuts import render
from .models import Student
from django.urls import reverse
from django.http import HttpResponseRedirect

from .forms import StudentForm
from .models import Student

# Create your views here.
def index(requset):
    students = Student.objects.all()
    if request.method=='POST':
        form=StudentForm(requset.PSOT)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = StudentForm()
    context = {
        'students':students,
        'form':form,
    }
    return render(requset,'index.html',context=context)