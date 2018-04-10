from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

user_list = [
    {'user':'jack','pwd':'abc'},
    {'user':'tom','pwd':'ABC'},
]

def index(request):
    if request.method == 'post':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        print(username,password)
    # request.POST
    # request.GET
    return render(request,'index.html',{'data':user_list})