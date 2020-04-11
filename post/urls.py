from django.urls import path
from django.conf.urls import url , include
from . import views

urlpatterns = [

    #path('', include('project.urls',namespace='myapp')),

    url(r'^$',views.signup,name='signup'),
    url(r'^login$',views.login_view,name='login'),
    url(r'^logout$',views.logout_view,name='logout')
    #url (r'^post2$',views.post2),
    #url(r'^$',views.signup,name='signup'),
    #url(r'^psot/$',views.post),


    ]
