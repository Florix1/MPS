from django.contrib import admin

from .models import (
	Contest,
	Team,
	Member,
	Category,
	)

admin.site.register(Contest)
admin.site.register(Team)
admin.site.register(Member)
admin.site.register(Category)