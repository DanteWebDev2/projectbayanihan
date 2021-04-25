from django.db import models

class Item(models.Model):

	#DONOR
	Donor = models.CharField(max_length=20, null=True)
	#EMAIL
	Email = models.CharField(max_length=20, null=True)
	#ITEM
	Donation= models.CharField(max_length=20, null=True)
	#SPECIFICS
	Items= models.CharField(max_length=20, null=True)
	#INSTRUCTIONS
	Message= models.TextField(max_length=50, null=True)

	click=(('button1','tion'),('button2','tion'))
	tion = models.CharField(max_length=10, choices=click, default='none')

	def __str__(self):
		return self.Donor
