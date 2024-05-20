from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index_html'),
    # path('firstindex.html', views.firstindex, name='firstindex_html'),
    path('studentregistration.html', views.studentregistration, name='studentregistration_html'),
    path('studentlogin.html', views.studentlogin, name='studentlogin_html'),
    path('studentdashboard.html', views.studentdashboard, name='studentdashboard_html'),
    path('studentcard.html', views.studentcard, name='studentcard_html'),
    path('studentlogout.html', views.studentlogout, name='studentlogout_html'),
    path('viewstudentcard.html', views.viewstudentcard, name='viewstudentcard_html'),

   ]