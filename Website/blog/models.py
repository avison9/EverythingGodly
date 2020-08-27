from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class post(models.Model):
	title = models.CharField(max_length = 100)
	author = models.ForeignKey(User, on_delete= models.CASCADE)
	content = models.TextField()
	date = models.DateTimeField(default=timezone.now)
	images = models.ImageField(default='default.jpg', upload_to='article_pic')

	def __str__(self):
		return self.title
		

	
