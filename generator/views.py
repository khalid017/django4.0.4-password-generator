from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generator\homepage.html')

def password(request):
    chars=list('abcdefghijklmnopqrtsuvwxyz')
    passw=''
    len= int(request.GET.get('length'))
    if request.GET.get('Uppercase'):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('Numbers'):
        chars.extend(list('0123456789'))
    if request.GET.get('Special'):
        chars.extend(list('!@#$%^&*()'))
    for i in range(len):
        passw=random.choice(chars)+passw
    return render(request,'generator\password.html',{'password':passw})

  