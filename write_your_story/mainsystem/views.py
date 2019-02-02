from django.shortcuts import render

# Create your views here.
def rootpage(request):
	return render(request,'root.html',None)