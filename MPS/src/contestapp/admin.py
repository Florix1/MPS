from django.contrib import admin

# Register your models here.

from .models import (
	Contest,
	Team,
	Category,
	Grade,
	Person,
	)

admin.site.register(Contest)
admin.site.register(Team)
admin.site.register(Category)
admin.site.register(Grade)
admin.site.register(Person)