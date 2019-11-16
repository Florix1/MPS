from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.forms import inlineformset_factory
from .forms import ContestPostModelForm

from contestapp.models import (
        Contest,
        Team,
        # Category,
        # Grade,
        Member,
    )


# Contest ===================================================================


@login_required(login_url='admin/login/?next=/')
def contest_post_list_view(request):
    qs = Contest.objects.all()
    template_name    = 'contest/list.html'
    context         = {'object_list': qs}
    return render(request, template_name, context)


@login_required(login_url='admin/login/?next=/')
def contest_post_create_view(request):
    form = ContestPostModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ContestPostModelForm()
    template_name    = 'contest/form.html'
    context         = {'form': form}
    return render(request, template_name, context)


@login_required(login_url='admin/login/?next=/')
def contest_post_detail_view(request, slug):
    obj = get_object_or_404(Contest, slug=slug)
    template_name    = 'contest/details.html'
    context         = {'object': obj}
    return render(request, template_name, context)


@login_required(login_url='admin/login/?next=/')
def contest_post_update_view(request, slug):
    obj = get_object_or_404(Contest, slug=slug)
    form = ContestPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name    = 'contest/update.html'
    context         = {'form': form}
    return render(request, template_name, context)


@login_required(login_url='admin/login/?next=/')
def contest_post_delete_view(request, slug):
    obj = get_object_or_404(Contest, slug=slug)
    template_name    = 'contest/delete.html'
    context         = {'object': obj}
    if request.method == "POST":
        obj.delete()
        return redirect("/")
    return render(request, template_name, context)


# # Category  =================================================================

# @login_required(login_url='admin/login/?next=/')
# def category_crud_post_view(request, slug):
#     obj                 = get_object_or_404(Contest, slug=slug)
#     template_name        = 'category/crud.html'
#     CategoryFormset        = inlineformset_factory(Contest, Category, fields=('name',), can_delete=True, extra=1, max_num=15)
    
#     if request.method == 'POST':
#         formset = CategoryFormset(request.POST, instance=obj)
#         if formset.is_valid():
#             formset.save()
#             return redirect(category_crud_post_view, slug=slug)

#     formset             = CategoryFormset(instance=obj)
#     context             = {'formset': formset}
#     return render(request, template_name, context)


# @login_required(login_url='admin/login/?next=/')
# def category_post_list_view(request, slug):
#     qs = Category.objects.filter(contest__slug=slug)
#     template_name    = 'category/list.html'
#     context         = {'object_list': qs}
#     return render(request, template_name, context)

# @login_required(login_url='admin/login/?next=/')
# def category_post_list_view1(request, slug, pk):
#     qs = Category.objects.filter(contest__slug=slug)
#     template_name    = 'category/list1.html'
#     context         = {'object_list': qs, 'slug':slug , 'pk': pk}
#     return render(request, template_name, context)

# Team ======================================================================


@login_required(login_url='admin/login/?next=/')
def team_list_post_view(request, slug):
    qs = Team.objects.filter(contest__slug=slug)
    template_name    = 'team/list.html'
    context         = {'object_list': qs}
    return render(request, template_name, context)


@login_required(login_url='admin/login/?next=/')
def team_crud_post_view(request, slug):
    obj                 = get_object_or_404(Contest, slug=slug)
    template_name        = 'team/crud.html'
    TeamFormset            = inlineformset_factory(Contest, Team, fields=('teamName', 'numberOnBack'), can_delete=True, extra=1, max_num=obj.membersPerTeam)
    
    if request.method == 'POST':
        formset = TeamFormset(request.POST, instance=obj)
        if formset.is_valid():
            formset.save()
            return redirect(team_crud_post_view, slug=slug)
    formset         = TeamFormset(instance=obj)
    context         = {'formset': formset}
    return render(request, template_name, context)


@login_required(login_url='admin/login/?next=/')
def team_post_detail_view(request, slug, pk):
    obj = get_object_or_404(Team, contest__slug=slug, pk=pk)
    template_name    = 'team/details.html'
    context         = {'object': obj}
    return render(request, template_name, context)


@login_required(login_url='admin/login/?next=/')
def team_post_delete_view(request, slug, pk):
    obj = get_object_or_404(Contest, contest__slug=slug, pk=pk)
    template_name    = 'team/delete.html'
    context         = {'object': obj}
    if request.method == "POST":
        obj.delete()
        return redirect("/")
    return render(request, template_name, context)


# # Grade =====================================================================


# @login_required(login_url='admin/login/?next=/')
# def grade_create_view(request):
#     form = ContestPostModelForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ContestPostModelForm()
#     template_name    = 'contest/form.html'
#     context         = {'form': form}
#     return render(request, template_name, context)


# @login_required(login_url='admin/login/?next=/')
# def grade_crud_view(request, slug, pk, c_pk):
#     obj                 = get_object_or_404(Category, pk=c_pk)
#     template_name        = 'grade/crud.html'
#     GradeFormset        = inlineformset_factory(Category, Grade, fields=('grade','comment','bonus'),can_delete=True, max_num=1)
    
#     if request.method == 'POST':
#         formset = GradeFormset(request.POST, instance=obj)
#         if formset.is_valid():
#             instances = formset.save(commit=False)
#             for instance in instances:
#                 instance.postedBy = request.user
#                 instance.save()
#             return redirect(grade_crud_view, slug=slug, pk=pk, c_pk=c_pk)
#     formset         = GradeFormset(instance=obj)
#     context         = {'formset': formset}
#     return render(request, template_name, context)


# Member ====================================================================


@login_required(login_url='admin/login/?next=/')
def member_crud_view(request, slug, pk):
    obj 				 = get_object_or_404(Team, pk=pk)
    template_name        = 'member/crud.html'
    MemberFormset        = inlineformset_factory(Team, Member, fields=('officialSurname','officialName','stageName','age',), can_delete=True, extra=1, max_num=obj.contest.membersPerTeam)
    
    if request.method == 'POST':
        formset = MemberFormset(request.POST, instance=obj)
        if formset.is_valid():
            formset.save()
            return redirect(member_crud_view, slug=slug, pk=pk)

    formset             = MemberFormset(instance=obj)
    context             = {'formset': formset}
    return render(request, template_name, context)


@login_required(login_url='admin/login/?next=/')
def member_list_view(request, slug, pk):
    qs = Member.objects.filter(team__pk=pk)
    template_name    = 'member/list.html'
    context         = {'object_list': qs, 'pk':pk}
    return render(request, template_name, context)


# # Extra =================================================================================================

# @login_required(login_url='admin/login/?next=/')
# def magic_button(request, slug):
#     team_qs    = Team.objects.filter(contest__slug=slug)
#     v = {}
#     for team in team_qs:
#         v[team.pk] = 0
#         grade_qs = Grade.objects.filter(teamName__pk=team.pk).filter(teamName__contest__slug=slug)
#         for gradez in grade_qs:
#             v[team.pk] += gradez.bonus
#             v[team.pk] += gradez.grade
#     maxim = 0
#     answer = team_qs.first()
#     for team in team_qs:
#         if team.isStillCompeting and not team.isDisqualified:
#                  if v[team.pk] > maxim:
#                     answer = team
#                     maxim = v[team.pk]
#     winners = Member.objects.filter(team__pk=answer.pk)
#     template_name   = 'rezultat.html'
#     context         = {'object': answer, 'winners': winners, 'score' : maxim}
#     return render(request, template_name, context)
