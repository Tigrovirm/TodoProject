from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def main_page(request):
	return HttpResponse("Hello World!")

def about_page(request):
	return HttpResponse("Burn to hell")