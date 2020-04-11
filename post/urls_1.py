from django.urls import path
from django.conf.urls import url , include
from . import views

urlpatterns = [

    #path('', include('project.urls',namespace='myapp')),
    
    url(r'^$',views.post),
    url (r'^post2$',views.post2),
    #url(r'^psot$',views.post),


    ]
