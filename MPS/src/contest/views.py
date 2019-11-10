from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.forms import inlineformset_factory
from .forms import ContestPostModelForm

from contestapp.models import (
		Contest,
		Team,
		Category,
		Grade,
		Person,
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

def category_create_update_post_view(request, slug):
	obj 				= get_object_or_404(Contest, slug=slug)
	template_name		= 'category/create_update.html'
	CategoryFormset		= inlineformset_factory(Contest, Category, fields=('name',))
	
	if request.method == 'POST':
		formset = CategoryFormset(request.POST, instance=obj)
		if formset.is_valid():
			formset.save()
			return redirect(category_create_update_post_view, slug=slug)

	formset 			= CategoryFormset(instance=obj)
	context 			= {'formset': formset}
	return render(request, template_name, context)

# Team ===================================================================


# Grade ===================================================================
