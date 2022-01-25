from django.db import models

# Create your models here.


class ClubType(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)

	def __str__(self):
		return str(self.name)

class Club(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	type = models.ForeignKey(ClubType,on_delete=models.CASCADE)

	def __str__(self):
		return str(self.name)

class BallPower(models.Model):
	value = models.IntegerField(max_length=200, blank=True, null=True)

	def __str__(self):
		return str(self.value)

class ClubLevel(models.Model):
	value = models.IntegerField(max_length=200, blank=True, null=True)

	def __str__(self):
		return str(self.value)