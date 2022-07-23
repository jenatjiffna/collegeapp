from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('next', views.next, name='next'),
    path('form1', views.StudentCreateView.as_view(), name='form1'),
    path('ajax/load-branches/', views.load_branches, name='ajax_load_branches'),
    path('ajax/load-fees/', views.load_fees, name='ajax_load_fees'),
    path('result1', views.result1, name='result1'),
   ]