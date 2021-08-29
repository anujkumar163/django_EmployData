from django.shortcuts import render
from .models import EmpData
from django.contrib import messages

# Create your views here.
def addrecord(request):
	if request.method == "POST":
	
		n = request.POST['nm']
		a = request.POST['age']
		addr = request.POST['addr']
		c = request.POST['city']

		e = EmpData(name=n, age=a, address=addr, city=c)
		e.save()
		messages.success(request, "employee added!")
		#return redirect('/employee/addrecord/')

	return render(request, "index.html")