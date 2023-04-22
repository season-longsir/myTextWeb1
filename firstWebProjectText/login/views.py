#from django.shortcuts import render
# 例：在login/views.py 中
from django.http import HttpResponse
# Create your views here.

from django.shortcuts import render,redirect
# Create your views here.
uap={'Season':'100201'}
def login(request):
  if request.method == 'POST':
     username = request.POST.get('username')
     passowrd = request.POST.get('password')
     #print(uap.keys())
     if username in uap.keys() and passowrd == uap.get(username,'111111'):
        return redirect('/index')
     else:
        return render(request,'login.html',{"error":"用户名或密码错误"})

  return render(request,'login.html')

def index(request):
  return render(request,'index.html')

def indexi(request):
  return redirect('/index')
