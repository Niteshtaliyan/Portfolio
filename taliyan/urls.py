from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='n4'),
    path('signup/', views.signup, name='n2'),
    path('login/', views.login, name='n3'),
    path('n1/', views.n1, name='n1'),
    path('single/', views.single, name='n5'),
    # url(r'^(?P<idd>[0-9]+)/$', views.index1, name='index1'),
    # url(r'^$', views.index, name='index'),
    

]