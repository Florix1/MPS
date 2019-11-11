from django.contrib.auth.decorators import login_required
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

@login_required(login_url='/admin')
def contest_post_list_view(request):
	qs = Contest.objects.all()
	template_name	= 'contest/list.html'
	context 		= {'object_list': qs}
	return render(request, template_name, context)


@login_required(login_url='/admin')
def contest_post_create_view(request):
	form = ContestPostModelForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ContestPostModelForm()
	template_name	= 'contest/form.html'
	context 		= {'form': form}
	return render(request, template_name, context)


@login_required(login_url='/admin')
def contest_post_detail_view(request, slug):
	obj = get_object_or_404(Contest, slug=slug)
	template_name	= 'contest/details.html'
	context 		= {'object': obj}
	return render(request, template_name, context)


@login_required(login_url='/admin')
def contest_post_update_view(request, slug):
	obj = get_object_or_404(Contest, slug=slug)
	form = ContestPostModelForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	template_name	= 'contest/form.html'
	context 		= {'form': form}
	return render(request, template_name, context)


@login_required(login_url='/admin')
def contest_post_delete_view(request, slug):
	obj = get_object_or_404(Contest, slug=slug)
	template_name	= 'contest/delete.html'
	context 		= {'object': obj}
	if request.method == "POST":
		obj.delete()
		return redirect("/")
	return render(request, template_name, context)



# Category  =================================================================

@login_required(login_url='/admin')
def category_crud_post_view(request, slug):
	obj 				= get_object_or_404(Contest, slug=slug)
	template_name		= 'category/crud.html'
	CategoryFormset		= inlineformset_factory(Contest, Category, fields=('name',), can_delete=True, extra=1, max_num=15)
	
	if request.method == 'POST':
		formset = CategoryFormset(request.POST, instance=obj)
		if formset.is_valid():
			formset.save()
			return redirect(category_crud_post_view, slug=slug)

	formset 			= CategoryFormset(instance=obj)
	context 			= {'formset': formset}
	return render(request, template_name, context)


@login_required(login_url='/admin')
def category_post_list_view(request, slug):
	qs = Category.objects.filter(contest__slug=slug)
	template_name	= 'category/list.html'
	context 		= {'object_list': qs}
	return render(request, template_name, context)

# Team ======================================================================

@login_required(login_url='/admin')
def team_list_post_view(request, slug):
	qs = Team.objects.filter(contest__slug=slug)
	template_name	= 'team/list.html'
	context 		= {'object_list': qs}
	return render(request, template_name, context)


@login_required(login_url='/admin')
def team_crud_post_view(request, slug):
	obj 				= get_object_or_404(Contest, slug=slug)
	template_name		= 'team/crud.html'
	TeamFormset			= inlineformset_factory(Contest, Team, fields=('teamName',), can_delete=True, extra=1, max_num=obj.membersPerTeam)
	
	if request.method == 'POST':
		formset = TeamFormset(request.POST, instance=obj)
		if formset.is_valid():
			formset.save()
			return redirect(team_crud_post_view, slug=slug)
	formset 		= TeamFormset(instance=obj)
	context 		= {'formset': formset}
	return render(request, template_name, context)


@login_required(login_url='/admin')
def team_post_detail_view(request, slug, pk):
	obj = get_object_or_404(Team, contest__slug=slug, pk=pk)
	template_name	= 'team/details.html'
	context 		= {'object': obj}
	return render(request, template_name, context)

#//TODO update and delete just like contest but with pk as parameter


@login_required(login_url='/admin')
def team_post_delete_view(request, slug, pk):
	obj = get_object_or_404(Contest, contest__slug=slug, pk=pk)
	template_name	= 'team/delete.html'
	context 		= {'object': obj}
	if request.method == "POST":
		obj.delete()
		return redirect("/")
	return render(request, template_name, context)


# Grade =====================================================================

#  team-category or category-team

# Person ====================================================================

#//TODO same as category just takes slug and pk as parameters

def person_list_view(request, slug, pk):
	pass

def person_crud_view(request, slug, pk):
	pass
	