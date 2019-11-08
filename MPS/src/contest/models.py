from django.db import models

# Create your models here.

class Contest(models.Model):
	title					=	models.CharField(max_length=max_len)
	teamCount				=	models.PositiveIntegerField()
	membersPerTeam			=	models.PositiveIntegerField()


class Team(models.Model):
	teamName			=	models.CharField(max_length=max_len)
	namesList			=	models.ArrayField(models.CharField(max_length=max_len), default=list, null=True)
	isDisqualified		=	models.BooleanField(default=False)
	isStillCompeting	=	models.BooleanField(default=True)
	contest             =   models.ForeignKey('Contest', relate_name='teams')


class Category(models.Model):
	name 				=	models.CharField(max_length=max_len)
	contest             =   models.ForeignKey('Contest', relate_name='categories')


class Grade(models.Model):
	categoryName 		=	models.ForeignKey('Category', relate_name='grades', on_delete=models.CASCADE)
	grade				=	models.PositiveIntegerField()
	postedBy			=	models.ForeignKey(User, on_delete=models.CASCADE)
	teamName 			=   models.ManyToManyField(Team)
	roundNumber			=	models.PositiveIntegerField()