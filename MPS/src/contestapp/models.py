from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils.text import slugify


class Contest(models.Model):
	title					=	models.CharField(max_length=50, unique=True)
	teamCount				=	models.PositiveIntegerField()
	membersPerTeam			=	models.PositiveIntegerField()
	slug 					=	models.SlugField(unique=True)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(Contest, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return f"/contest/{self.slug}"

	def get_edit_url(self):
		return f"/contest/{self.slug}/update"

	def get_delete_url(self):
		return f"/contest/{self.slug}/delete"


class Team(models.Model):
	teamName			=	models.CharField(max_length=30)
	isDisqualified		=	models.BooleanField(default=False)
	isStillCompeting	=	models.BooleanField(default=True)
	contest             =   models.ForeignKey('Contest', related_name='teams', on_delete=models.CASCADE)

	def __str__(self):
		return self.teamName

class Category(models.Model):
	name 				=	models.CharField(max_length=20)
	contest             =   models.ForeignKey('Contest', related_name='categories', on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Grade(models.Model):
	categoryName 		=	models.ForeignKey('Category', related_name='grades', on_delete=models.CASCADE)
	grade				=	models.PositiveIntegerField(default=0)
	postedBy			=	models.ForeignKey(User, on_delete=models.CASCADE)
	teamName 			=   models.ManyToManyField(Team)
	roundNumber			=	models.PositiveIntegerField()

	def __str__(self):
		return 'Nota_' + self.teamName + '_' + self.categoryName

class Person(models.Model):
	name 				=	models.CharField(max_length=30)
	age 				=	models.PositiveIntegerField()
	team 				=	models.ForeignKey('Team', related_name='persons', on_delete=models.CASCADE)

	def __str__(self):
		return self.name