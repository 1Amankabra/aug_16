from datetime import datetime,timedelta 
from django.shortcuts import render




# Create your views here.
def setcookie(request):
 response = render(request,'student/setcookies.html')
 #response.set_cookie('name','aman',max_age=120)#will alive for 120 sec = 2 min
 response.set_cookie('name','aman',expires=datetime.utcnow()+timedelta(days=3))
 return response

def getcookie(request):
 #name = request.COOKIES['name']
 #name = request.COOKIES.get('name')
 name = request.COOKIES.get('name','XYZ')
 return render(request,'student/getcookies.html',{'name':name}) 

def deletecookie(request):
 response = render(request,'student/deletecookies.html')
 #response.set_cookie('name','aman',max_age=120)#will alive for 120 sec = 2 min
 response.delete_cookie('name')
 return response 