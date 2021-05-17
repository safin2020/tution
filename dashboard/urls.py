from django.urls import path
from dashboard import views	

app_name = 'tution'
urlpatterns = [
    path('',views.dashboard , name='dashboard' ),

]