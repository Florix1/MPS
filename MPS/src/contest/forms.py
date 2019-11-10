from django import forms

from contestapp.models import Contest
from contestapp.models import Team
from contestapp.models import Grade

class ContestPostModelForm(forms.ModelForm):
	class Meta:
		model = Contest
		fields = ['title', 'teamCount', 'membersPerTeam']

	def clean_title(self, *args, **kwargs):
		title = self.cleaned_data.get('title')
		qs = Contest.objects.filter(title__iexact=title)
		if qs.exists():
			raise forms.ValidationError("This contest title has already been used.\nPlease try again.")
		return title

	def clean_teamCount(self, *args, **kwargs):
		teamCount = self.cleaned_data.get('teamCount')
		if teamCount < 5 or teamCount > 20:
			raise forms.ValidationError("Must be a number between 5 and 20.\nPlease try again")
		return teamCount

	def clean_membersPerTeam(self, *args, **kwargs):
		membersPerTeam = self.cleaned_data.get('membersPerTeam')
		if membersPerTeam < 2 or membersPerTeam > 5:
			raise forms.ValidationError("Must be a number between 2 and 5.\nPlease try again")
		return membersPerTeam

class TeamPostModelForm(forms.ModelForm):
	class Meta:
		model = Team
		fields = ['teamName', 'isDisqualified', 'isStillCompeting', 'contest']

	def clean_teamName(self, *args, **kwargs):
		teamName = self.cleaned_data.get('teamName')
		qs = Team.objects.filter(title__iexact=teamName)
		if qs.exists():
			raise forms.ValidationError("This team name has already been used.\nPlease try again.")
		return teamName

class GradePostModelForm(forms.ModelForm):
	class Meta:
		model = Grade
		fields = ['categoryName', 'grade', 'postedBy', 'teamName', 'roundNumber']

	def clean_grade(self, *args, **kwargs):
		grade = self.cleaned_data.get('grade')
		if grade < 0 or grade > 10:
			raise forms.ValidationError("Grade is not valid.\nPlease try again")
		return grade