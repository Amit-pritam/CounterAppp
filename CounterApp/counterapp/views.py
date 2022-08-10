from django.shortcuts import render,redirect
from .models import CounterModel


def index(request):                                   #index view with a variable "obj" where we get  the no by using filter  query.
	name = 'Amit'
	obj = CounterModel.objects.filter(id = 1).first() #we always use first with filter  query.
	ournumber = obj.number                            #take another variable "ournumber".
	context = {'name': name, 'number': ournumber}     #context always writen in dictonary format
	return render(request,"index.html",context)       #render function is used for rendering template. 


def increment(request):                               #This is the view for  Incriment.
	obj = CounterModel.objects.get(id = 1)            #Querry to get  that number.
	obj.number=int(obj.number) + 1                    #number incrised by one.
	obj.save()                                        #query  to save  tha number
	return redirect(request.META['HTTP_REFERER'])     #to redirect on the same page we use this.



def reset(request):                                    #view for Reset.
	obj = CounterModel.objects.get(id = 1)             #querry to get that number.
	obj.number = 0                                     #number become ZERO.
	obj.save()
	return redirect(request.META['HTTP_REFERER'])



def decrement(request):                                #view function for decriment.
	obj = CounterModel.objects.get(id=1)               #query to get that number.
	obj.number = int(obj.number) - 1                   #decrease the number by One.
	obj.save()
	return redirect(request.META['HTTP_REFERER'])


