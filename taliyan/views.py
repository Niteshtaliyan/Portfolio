from django.shortcuts import render, loader
from django.http import HttpResponse
from .models import table1

# Create your views here.

def index(request):
    #return HtpResponse("</h1>HEEELLLOO<h1>")
    all_data=table1.objects.all()
    context={
    'all_data':all_data,
    }
    return render(request,'basic.html',context)

def index1(request,idd):
#return HtpResponse("WELVCOME"+ str(idd))
    m1=table1.objects.get(pk=idd)
    return render(request,'basic.html',{'m1':m1,'idd':idd})

def reg(request):
    if request.method == 'POST':
        data1=request.POST.get('nm','')
        data2=request.POST.get('em','')
        data3=request.POST.get('ps','')
        song_obj=table1(username=data1,email=data2,password=data3)
        song_obj.save()
        return render(request, 'form.html',context)
    else:
        return render(request, 'signup.html')



def index(request):
    return render(request,'index.html',{})

def signup(request):
    if request.method == 'POST':
        data1=request.POST.get('fullname','')
        data2=request.POST.get('phone','')
        data3=request.POST.get('address','')
        data4=request.POST.get('email','')
        data5=request.POST.get('ps','')
        data6=request.POST.get('re_pass','')
        data7=request.POST.get('file','')
        data8=request.POST.get('agree_term','')

        song_obj=table1(fullname=data1,phone=data2,address=data3,email=data4,ps=data5,re_pass=data6,file=data7,agree_term=data8)
        song_obj.save()
        return render(request, 'index.html')
    else:
        return render(request, 'signup.html')


def login(request):
    return render(request,'login.html',{})

def n1(request):
    return render(request,'n1.html',{})

def single(request):
    return render(request,'single.html',{})



