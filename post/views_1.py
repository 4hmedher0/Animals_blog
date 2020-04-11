from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def post(request):
    #return HttpResponse('Post page')
    return render (request,'post.html')
def post2(request):
    return HttpResponse('Post page2')
