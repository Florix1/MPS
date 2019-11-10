from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from contestapp.models import (
		Contest,
		Team,
		Category,
		Grade,
	)

def contest_post_list_view(request):
	qs = Contest.objects.all()
	template_name	= 'contest_list.html'
	context 		= {'object_list': qs}
	return render(request, template_name, context)


def contest_post_create_view(request):
	form = ContestPostModelForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ContestPostModelForm()
	template_name	= 'contest_form.html'
	context 		= {'form': form}
	return render(request, template_name, context)


def contest_post_detail_view(request, slug):
	obj = get_object_or_404(Contest, slug=slug)
	template_name	= 'contest_detail.html'
	context 		= {'form': form}
	return render(request, template_name, context)


def contest_post_update_view(request):
	form = ContestPostModelForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ContestPostModelForm()
	template_name	= 'contest_update.html'
	context 		= {'form': form}
	return render(request, template_name, context)


def contest_post_delete_view(request, slug):
	form = ContestPostModelForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ContestPostModelForm()
	template_name	= 'contests_delete.html'
	context 		= {'form': form}
	return render(request, template_name, context)