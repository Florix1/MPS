from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ContestPostModelForm

from contestapp.models import (
		Contest,
		Team,
		Category,
		Grade,
	)

# Contest ===================================================================

def contest_post_list_view(request):
	qs = Contest.objects.all()
	template_name	= 'contest/list.html'
	context 		= {'object_list': qs}
	return render(request, template_name, context)


def contest_post_create_view(request):
	form = ContestPostModelForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ContestPostModelForm()
	template_name	= 'contest/form.html'
	context 		= {'form': form}
	return render(request, template_name, context)


def contest_post_detail_view(request, slug):
	obj = get_object_or_404(Contest, slug=slug)
	template_name	= 'contest/details.html'
	context 		= {'object': obj}
	return render(request, template_name, context)


def contest_post_update_view(request, slug):
	obj = get_object_or_404(Contest, slug=slug)
	form = ContestPostModelForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	template_name	= 'contest/form.html'
	context 		= {'form': form}
	return render(request, template_name, context)


def contest_post_delete_view(request, slug):
	obj = get_object_or_404(Contest, slug=slug)
	template_name	= 'contests/delete.html'
	context 		= {'object': obj}
	if request.method == "POST":
		obj.delete()
		return redirect("/")
	return render(request, template_name, context)



# Category ===================================================================


# Team ===================================================================


# Grade ===================================================================
