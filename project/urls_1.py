"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.conf.urls import url , include
from myapp import views
from myapp.views import homepage
from django.views import View
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('project.urls',namespace='myapp')),
    url(r'^$' ,views.home,name='home'),
    #url(r'^',include('post.urls'),
    url(r'^myapp', views.source,name='source'),
    url(r'^homepage', views.homepage,name='homepage'),
    url(r'^hw$' ,views.hw,name='hw'),
    url(r'^post2',include('post.urls'),name='post2'),
    url(r'^post',include('post.urls'),name='post'),
    url(r'^time$', views.timenow ,name='timenow' ),
    url(r'^(?P<catch>[\w]+)/$', views.catch ,name='catch'), # CATCH UNEXPECTED URL
    #url(r'^time/plus/(\d+)/$',views.plustime),
    url(r'^time/plus/(\d{1,3})/$',views.plustime),
    url(r'^create$', views.create ,name='create' ),
    url(r'^edit/(?P<id>\d+)/$',views.editform , name='editforms'),
    url(r'^all_posts$', views.show_all_posts , name='all_posts' ),
    # url(r'^all_posts/<int:id>/$', views.show_one_post , name='one_post' ),
     url(r'^all_posts/(?P<offset>[\w-]+)/$', views.show_one_post , name='one_post' ),

    #url(r'^onepost$', views.show_one_post ),
    url(r'^add/(\d{1,9})/$',views.catchnum),




    #url(r'^vaccine$' ,views.vaccine,name='vaccine'),
    #url(r'^$',include('post.urls'),name='post'),


    #url(r'^create$' ,views.createform,name='createform')
    #url(r'^create', views.ctreateform,name='createform'),

    #url(r'^animal_details', views.animal_details,name='animal_details')

    # url(r'^animal/(\d+)/$' , views.animal_detail ,name='animal_detail')
    #url(r'^myapp/(\d+)/',views.animal_detail,name='animal_detail'),
]
urlpatterns +=staticfiles_urlpatterns()
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
