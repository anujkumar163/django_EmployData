from django.db import models

# Create your models here.
class Dept(models.Model):
	dname = models.CharField(max_length=20)
	block= models.CharField(max_length=20)
	capacitySH = models.IntegerField()
