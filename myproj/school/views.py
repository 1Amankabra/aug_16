from django.shortcuts import render

# # Create your views here.
# def model_view(request):
#     student = {'name':'aman'}
#     return render(request,'.html',{'data':student})

from django.views.generic.list import ListView
from .models import Student

class StudentLListView(ListView):
 model = Student
 #template_name_suffix = '_get'
 template_name= 'school/student.html'
 #ordering =['name']
 context_object_name = 'students'

def get_queryset(self):
    return Student.objects.filter(course='pd')

def get_context_data(self, **kwargs):
 context=super().get_context_data(**kwargs)
 context['freshers']=Student.objects.all().order_by('name').order_by('course')
 return context    

def get_template_names(self):
  if self.request.user.is_superuser:
     template_name = 'school/superuser.html'
  elif self.request.user.is_staff:
      template_name='school/staff.html'   
  else:
     template_name = self.template_name
  return [template_name]
