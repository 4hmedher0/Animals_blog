from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login,logout


# Create your views here.


def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST or None)
        if form.is_valid :
            user=form.save()
            login(request,user)

            #messages.success(request, 'Done.')
            return redirect ('/')
    else:
        form=UserCreationForm()
        return render (request,'signup.html',{'signup':form})

def post(request):
    return render (request,'signup.html')


def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST) #pass data for test
        if form.is_valid():
            messages.info(request, 'Passed.')
            user=form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/')
    else:
        #ht='Wrong password or username try again'
        form=AuthenticationForm()
        messages.info(request, 'Wrong password or username try again.')

    return render(request,'login.html',{'login':form})

    #return HttpResponse('login form page ')
'''def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('all_posts')
    else:
        return HttpResponse('DoesNotWork')
'''

def logout_view(request):
    logout(request)
    messages.info(request,'logged out success')
    return redirect('all_posts')
'''

#create new User

def signup(request):
    form=UserCreationForm()
    return render (request,'signup.html',{'signup':form})
'''
