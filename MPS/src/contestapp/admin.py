from django.contrib import admin

from .models import (
	Contest,
	Team,
	)

admin.site.register(Contest)
admin.site.register(Team)