
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.


class Contest(models.Model):
	title					=	models.CharField(max_length=50)
	teamCount				=	models.PositiveIntegerField()
	membersPerTeam			=	models.PositiveIntegerField()


class Team(models.Model):
	teamName			=	models.CharField(max_length=50)
	#//TODO 1 Contender (similar to category)
	isDisqualified		=	models.BooleanField(default=False)
	isStillCompeting	=	models.BooleanField(default=True)
	contest             =   models.ForeignKey('Contest', related_name='teams', on_delete=models.CASCADE)


class Category(models.Model):
	name 				=	models.CharField(max_length=50)
	contest             =   models.ForeignKey('Contest', related_name='categories', on_delete=models.CASCADE)


class Grade(models.Model):
	categoryName 		=	models.ForeignKey('Category', related_name='grades', on_delete=models.CASCADE)
	grade				=	models.PositiveIntegerField()
	postedBy			=	models.ForeignKey(User, on_delete=models.CASCADE)
	teamName 			=   models.ManyToManyField(Team)
	roundNumber			=	models.PositiveIntegerField()
	comment				=	models.CharField(max_length=150, default='Nothing to add.', null=True)