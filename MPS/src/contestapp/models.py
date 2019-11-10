from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils.text import slugify


class Contest(models.Model):
	title					=	models.CharField(max_length=50, unique=True)
	teamCount				=	models.PositiveIntegerField()
	membersPerTeam			=	models.PositiveIntegerField()
	slug 					=	models.SlugField(unique=True)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(Contest, self).save(*args, **kwargs)


class Team(models.Model):
	teamName			=	models.CharField(max_length=30)
	isDisqualified		=	models.BooleanField(default=False)
	isStillCompeting	=	models.BooleanField(default=True)
	contest             =   models.ForeignKey('Contest', related_name='teams', on_delete=models.CASCADE)


class Category(models.Model):
	name 				=	models.CharField(max_length=20)
	contest             =   models.ForeignKey('Contest', related_name='categories', on_delete=models.CASCADE)


class Grade(models.Model):
	categoryName 		=	models.ForeignKey('Category', related_name='grades', on_delete=models.CASCADE)
	grade				=	models.PositiveIntegerField()
	postedBy			=	models.ForeignKey(User, on_delete=models.CASCADE)
	teamName 			=   models.ManyToManyField(Team)
	roundNumber			=	models.PositiveIntegerField()

class Person(models.Model):
	name 				=	models.CharField(max_length=30)
	age 				=	models.PositiveIntegerField()
	team 				=	models.ForeignKey('Team', related_name='persons', on_delete=models.CASCADE)