from django.db import models


class Crop(models.Model):
	crop_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	price = models.FloatField(default=0)
	def __str__(self):
		return self.crop_text

class Choice(models.Model):
	crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	def __str__(self):
		return self.choice_text