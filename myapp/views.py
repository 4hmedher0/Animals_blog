from django.shortcuts import render ,redirect ,get_object_or_404
from django.http import HttpResponse
from django.http import Http404
import datetime
from .forms import AnimalForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import animal


#from .modles import vaccine
# Create your views here.
def home(request):
    Animals=animal.objects.all()
    return render(request,'home.html',{'Animals':Animals})


def source (request,id=id):
    #return HttpResponse('<p>Source function</p>'.format(id))
    try:
        # animal=animal.objects.all()
          return render (request,'base.html',{'animal':animal})
    except animal.DoesNotExis :
        raise Http404('TRY AGAIN')
        return render (request,'animal_details.html',{'animal':animal})
def animal_details (request ,id):
    Vaccines=vaccine.objects.get(id=id)
    context={'Vaccines':Vaccines}
    return render (request ,'animal_details.html',context)

#def createform (request):
#    pass
    #render(request ,createform.html, 'createform':createform)
def hw (request):
    animals=animal.objects.all().order_by('name')
    return render(request ,'hw.html',{'animals':animals})

def timenow (request):
    dt=datetime.datetime.now()
    html="time now is %s" %dt
    return HttpResponse(html)

def catch(request,catch):
    #ht="this page DoesNotExis   '%s'" %(catch)
    #return HttpResponse(ht)
    animals=animal.objects.get(name=catch)
    return render(request,'test.html',{'animals':animals})

def catchnum(request,offset):

    try:
      offset=int(offset)
    except:
      raise Http404()
    #return HttpResponse(offset)
    animals=animal.objects.get(age=offset)
    return render(request,'test.html',{'animals':animals})

def plustime(request , offset ):
    try:
        offset=int(offset)
    except:
        raise Http404()
    dt=datetime.datetime.now()
    plusdt=datetime.datetime.now() + datetime.timedelta(hours=offset)
    html="time now is %s  and time after %s  is %s "%(dt,offset,plusdt)
    return HttpResponse(html)
@login_required(login_url="/postsignup/login")
def create (request):
    form=AnimalForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.author=request.user
        instance.save()
        #form.save()
        messages.success(request,'Done.')
        return redirect('/')

    return render(request,'form.html',{'form':form})
@login_required(login_url="/postsignup/login")
def editform (request,id):
    animals=get_object_or_404(animal,id=id)
    form=AnimalForm(request,instance=animal)
    if request.method =='POST':
        if form.is_valid():
            form=AnimalForm(request.POST or None , instance=animal )
            form.save()
            return redirect('/')

    else:
        form=AnimalForm(instance=animal)
        #return redirect('/')
    return render(request,'editform.html',{'form':form, 'animals':animal})

 
def show_all_posts(request):
    animals=animal.objects.all().order_by('name')
    return render (request ,'bootstrapall.html',{'animals':animals})

def show_one_post(request,offset):
    offset=int(offset)
    animals=animal.objects.get(id=offset)
    #offset=animal.id
    #return render (request ,'bootstrapone.html',{'animals':animals})
    return render (request ,'bootstrapone.html',{'animals':animals ,'offset':offset})




    #return HttpResponse('hw')
    #animals=animal.objects.all()
    #context={'animal':animal}
    #return render (request ,'animal_details.html',context)
#def vaccine(request):
#    vaccines=vaccine.objects.all()
#    return render(request , 'vaccine.html' , {'vaccines':vaccines})
class homepage():
    def get(self,request):
         return HttpResponse("wellcome مرحبا")
        #return render(request,'animal_details.html',{'Animals':Animals})
