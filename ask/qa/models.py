from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateField(auto_now_add=True)
	rating = models.IntegerField()
	author = models.ForeignKey(User, related_name='question_author')
	likes = models.ManyToManyField(User, related_name='question_likes')
	
	class Meta:
		db_table = 'question'
	
class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateField(auto_now_add=True)
	question = models.ForeignKey(Question)
	author = models.ForeignKey(User, related_name='answer_author')
	
	class Meta:
		db_table = 'answer'