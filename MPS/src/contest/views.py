from django.http import HttpResponse
from django.shortcuts import render

# from .models import (
# 		Contest,
# 		Team,
# 		Category,
# 		Grade,
# 	)

def home_page(request):
	template_name	= 'home_page.html'
	context 		= {}
	return render(request, template_name, context)

def teams(request):
	template_name	= 'teams.html'
	context 		= {}
	return render(request, template_name, context)

def ranking(request):
	template_name	= 'ranking.html'
	context 		= {}
	return render(request, template_name, context)

def competitions(request):
	template_name	= 'competitions.html'
	context 		= {}
	return render(request, template_name, context)