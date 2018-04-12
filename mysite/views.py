from django.shortcuts import render
from mysite import models
# Create your views here.


def index(request):
    if request.method == 'post':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
    #添加数据到数据库
    models.UserInfo.objects.create(user=username,pwd=password)
    #从数据库中读取所有数据
    user_list = models.UserInfo.objects.all()

    return render(request,'index.html',{'data':user_list})