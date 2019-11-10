from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Contest(models.Model):
	title					=	models.CharField(max_length=50)
	teamCount				=	models.PositiveIntegerField()
	membersPerTeam			=	models.PositiveIntegerField()


class Team(models.Model):
	teamName			=	models.CharField(max_length=30)
	#//TODO namesList			=	models.ArrayField(models.CharField(max_length=40), default=list, null=True)
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