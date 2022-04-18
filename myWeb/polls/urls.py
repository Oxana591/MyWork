from django.urls import path

from . import views

urlpatterns = [
    path('site1/', views.index, name='index'),
    path('time',views.func1,name='func1'),
    path("<str:name>",views.hi,name='hi')
]