from django.db import forms

from contestapp.models import Contest

class ContestPostModelForm(forms.ModelForm):
	class Meta:
		model = Contest
		fields = ['title', 'teamCount', 'membersPerTeam']