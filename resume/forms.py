from django import forms
from matplotlib import widgets
from .models import Emp_resume

JOB_CITY = [
    ('mumbai','mumbai'),
    ('delhi','delhi'),
    ('pune','pune'),
]



class Resumeform(forms.ModelForm):
    job_city = forms.MultipleChoiceField(label='preferred job locations',choices=JOB_CITY,widget= forms.CheckboxSelectMultiple)
    class Meta:
        model = Emp_resume
        fields = ['name','dob','gender','locality','city','pin','state','mobile','email','job_city','profile_img','my_file']
        labels = {
            'name':'Full name','dob':'Date of birth','gender':'Gender','locality':'Locality','city':'City','pin':'Pin','state':'State','mobile':'Mobile','email':'Email','job_city':'prefered location',
            'profile_img':'Upload image','my_file':'Document upload',
        }

        widgets= {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'dob': forms.DateInput(attrs={'class':'form-control','placeholder':'MM/DD/YYY'}),
            'gender': forms.Select(attrs={'class':'form-select'}),
            'locality': forms.TextInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'pin': forms.NumberInput(attrs={'class':'form-control'}),
            'state': forms.Select(attrs={'class':'form-select'}),
            'mobile': forms.NumberInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            
            
            
        }