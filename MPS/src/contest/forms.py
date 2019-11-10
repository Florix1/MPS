from django import forms

from contestapp.models import Contest

class ContestPostModelForm(forms.ModelForm):
	class Meta:
		model = Contest
		fields = ['title', 'teamCount', 'membersPerTeam']

	#//TODO 2 Need to add validation to fields