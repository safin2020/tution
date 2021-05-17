from django.shortcuts import render
from .models import JoiningClass
# Create your views here.
def dashboard(request):
	details = JoiningClass.objects.filter(active=True)
	noclasstext = JoiningClass.objects.all()
	context = {
		'details':details ,
		'noclasstext':noclasstext 
	}
	return render(request,'dashboard/index.html',context)