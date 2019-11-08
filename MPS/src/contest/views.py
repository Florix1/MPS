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