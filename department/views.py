from django.shortcuts import render
from .forms import DeptForm

# Create your views here.
def add_dept(request):
	df = DeptForm(request.POST)
	if request.method == "POST":
		if df.is_valid():
			df.save()
	
		messages.success(request, "employee added!")
		
	return render(request, "add_dept.html", {'data': df})

'''def add_show(request):
	if request.method == 'POST':
		fm = studentRegistration(request.POST)
		if fm.is_valid():
			nm = fm.cleaned_data['name']
			em = fm.cleaned_data['email']
			pw = fm.cleaned_data['password']
			reg = user(name=nm, email=em, password=pw)
			reg.save()
			fm = studentRegistration()'''