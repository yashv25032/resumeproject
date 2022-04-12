from django.shortcuts import redirect, render
from resume.forms import Resumeform
from .models import Emp_resume
  
# Create your views here.
def Myresume(request):
    form = Resumeform()
    if request.method == 'POST':
        form = Resumeform(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Resumeform() 
    sm = Emp_resume.objects.all()   


    return render(request,"home.html",{'forms':form,'sms':sm})



def candilist(request,pk):
    fm = Emp_resume.objects.get(pk= pk)
    return render(request,"candidate.html",{'dm':fm})