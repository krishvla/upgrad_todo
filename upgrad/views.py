from django.shortcuts import render,redirect
from .models import todo as td, Category
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
import datetime
from datetime import timedelta
from django.utils import timezone
from .tasks import test

job = test.delay()

def index(request):
	if request.user.is_authenticated: #quering all todos with the object manager
	    user = request.user
	    mail = user.email
	    print("mail is",mail)
	    categories = Category.objects.all() #getting all categories with object manager
	    list_todo = td.objects.all()
	    if request.method == "POST": #checking if the request method is a POST
	        if "taskAdd" in request.POST: #checking if there is a request to add a todo
	            title = request.POST["description"] #title
	            date = str(request.POST["date"]) #date
	            category = request.POST["category_select"] #category
	            content = title + " -- " + date + " " + category #content
	            Todo = td(title=title, content=content, due_date=date, gmail=mail, category=Category.objects.get(name=category))
	            Todo.save() #saving the todo 
	            return redirect(index) #reloading the page
	        if "delete" in request.POST: #checking if there is a request to delete a todo
	            list_id = request.POST["delete_id"]
	            print("The list_id is: - ",list_id)
	            Todo = td.objects.get(t_id=list_id)
	            Todo.delete()
	            Todo.save()
	return render(request, "index.html", { "list_todo":list_todo, "categories":categories})



def delete_list(request, pk):
    Todo = td.objects.get(t_id=pk)
    print("The list_id is: - ",Todo)
    td.objects.filter(t_id=pk).delete()
    return redirect(index)

def update_list(request, pk):
    list_todo = td.objects.get(t_id=pk)
    categories = Category.objects.all()
    if "update_li" in request.POST:
    	tit = request.POST["description"] #title
    	dat = str(request.POST["date"]) #date
    	categ = request.POST["category_select"] #category
    	cont = tit + " -- " + dat + " " + categ #content
    	td.objects.filter(t_id = pk).update(title = tit, content = cont, due_date = dat, category=Category.objects.get(name=categ), status = 'F')
    	return redirect(index)
    return render(request, "update.html", { "list_todo":list_todo, "categories":categories})


def alogin(request):
	if "signup" in request.POST:
		fname = request.POST["firstname"]
		lname = request.POST["lastname"]
		mail = request.POST["gmail"]
		pas = request.POST["password"]
		uname = request.POST["username"]
		use = User.objects.create_user(first_name=fname, last_name='lname', username=uname, password=pas, email=mail)
		use.save()
		return redirect(alogin)
	elif "alogin" in request.POST:
		uname = request.POST['user_id']
		pas = request.POST['password']
		user = authenticate(request, username=uname, password=pas)
		print("The thing is:",user)
		if user is not None:
			login(request, user)
			return redirect(index)
		else:
			print("Wrong credintials")
			return redirect(alogin)

	return render(request,"login.html")



def logout_view(request):
	logout(request)
	return redirect(alogin)
