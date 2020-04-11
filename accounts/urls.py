from django.urls import path
from django.conf.urls import url , include
from . import views

urlpatterns = [

    #path('', include('project.urls',namespace='myapp')),

    url(r'^$',views.signup),
    url (r'^url$',views.signup),
    #url(r'^psot$',views.post),


    ]
