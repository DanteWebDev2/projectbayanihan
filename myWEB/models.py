from django.db import models


class Guests(models.Model):

	#GUEST
	Guest = models.CharField(max_length=20, null=True)

	def __str__(self):
		return self.Guest


class Members(models.Model):

	#MEMBER
	Member = models.CharField(max_length=20, null=True)

	def __str__(self):
		return self.Member


class Enter(models.Model):

	#NAME OF MEMBER
	Username = models.CharField(max_length=20, null=True)
	#PASSWORD OF MEMBER
	Password = models.CharField(max_length=20, null=True)
	
	def __str__(self):
		return self.Username


class Sponsor(models.Model):

	#FIRST NAME
	First = models.CharField(max_length=20, null=True)
	#LAST NAME
	Surname = models.CharField(max_length=20, null=True)
	#EMAIL ADDRESS
	Email= models.EmailField(max_length=20, null=True)
	#PHONE NUMBER
	Contact= models.IntegerField(null=True)
	#STREET ADDRESS
	Address= models.CharField(max_length=50, null=True)

	def __str__(self):
		return self.First


class Option(models.Model):

	sponsors=models.ForeignKey(Sponsor, default=None, on_delete=models.CASCADE, null=True)
	enters=models.ForeignKey(Enter, default=None, on_delete=models.CASCADE, null=True)

	choose =(('Monetary Donation', 'Monetary Donation'), ('In-Kind Donation', 'In-Kind Donation'))
	Donors = models.CharField(max_length=20, choices=choose, null=True)

	#SPONSOR NOTE
	Message= models.TextField(max_length=50, null=True)

	def __str__(self):
		return self.Donors


class Monetary(models.Model):

	viewer=models.ManyToManyField(Sponsor)

	#SPECIFY YOUR DONATION
	List = models.CharField(max_length=20, null=True)
	#WISH TO DONATE
	Amount = models.CharField(max_length=20, null=True)
	#GCASH ACCOUNT
	Gcash= models.CharField(max_length=20, null=True)
	#BANK ACCOUNT
	Bank= models.CharField(max_length=20, null=True)
	#BILLING ADDRESS
	Bills= models.TextField(max_length=50, null=True)

	def __str__(self):
		return self.List


class Transaction(models.Model):

	viewer=models.ForeignKey(Sponsor, default=None, on_delete=models.CASCADE, null=True)
	#DESTINATION
	Place = models.CharField(max_length=20, null=True)
	#CHARGING FEE
	Fee = models.IntegerField(null=True)
	
	def __str__(self):
		return self.Place
		

class Inkind(models.Model):

	viewer=models.ManyToManyField(Sponsor)

	#FOOD NECESSITIES
	Food = models.CharField(max_length=20, null=True)
	#BEVERAGES
	Drinks = models.CharField(max_length=20, null=True)
	#HYGIENE
	Sanitation= models.CharField(max_length=20, null=True)
	#MEDICINE
	Cure= models.CharField(max_length=20, null=True)

	#FOOD QUANTITY
	Count = models.IntegerField(null=True)
	#BEVERAGES QUANTITY
	Count1= models.IntegerField(null=True)
	#HYGIENE QUANTITY
	Count2= models.IntegerField(null=True)
	#MEDICINE QUANTITY
	Count3= models.IntegerField(null=True)


	def __str__(self):
		return self.Food
		

class Settlement(models.Model):

	viewer=models.ForeignKey(Sponsor, default=None, on_delete=models.CASCADE, null=True)

	#PICK-UP LOCATION
	Locations = models.CharField(max_length=20, null=True)
	#DESTINATIONS
	Places=(('Metro Manila', 'Metro Manila'), ('Luzon', 'Luzon'), ('Visayas', 'Visayas'), ('Mindanao','Mindanao'), ('Overseas', 'Overseas'))
	#CHARGING FEE
	Charges = models.IntegerField(null=True)


	def __str__(self):
		return self.Locations