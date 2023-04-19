from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
# Create your views here.

tasks = {"task_1": "Убери комнату", "task_2": "Купи продукты"}

def index(request):
	todos = Todo.objects.all()
	return render(request, "Syx.html", {"todos": todos})

def about_page(request):
	return HttpResponse("Burn to hell")