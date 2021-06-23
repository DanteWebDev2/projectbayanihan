from django.db import models


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

	choose =(('Monetary Donation', 'Monetary Donation'), ('In-Kind Donation', 'In-Kind Donation'), ('Both Donation', 'Both Donation'))
	Donors = models.CharField(max_length=20, choices=choose, null=True)

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


class Fundraising(models.Model):

	viewer=models.ForeignKey(Sponsor, default=None, on_delete=models.CASCADE, null=True)

	#ORGANIZATION NAME
	Organization = models.CharField(max_length=20, null=True)
	#ORGANIZATION'S CONTACT PERSON
	Organizer = models.CharField(max_length=20, null=True)
	#EVENT NAME
	Event= models.CharField(max_length=20, null=True)
	#LOCATION ADDRESS
	Area= models.CharField(max_length=50, null=True)
	#MAILING ADDRESS
	Email= models.EmailField(max_length=20, null=True)
	#DATE NEEDED
	Time= models.DateField(max_length=20, null=True)
	#Items NEEDED
	Item= models.CharField(max_length=20, null=True)
	#QUANTITY NEEDED
	Sum= models.IntegerField(null=True)


	def __str__(self):
		return self.Fund


class Recipient(models.Model):

	viewer=models.ForeignKey(Sponsor, default=None, on_delete=models.CASCADE, null=True)

	#DONATION RECIPIENT
	Receiver = models.CharField(max_length=20, null=True)
	#DATE RECEIVE
	Dates = models.DateField(max_length=20, null=True)
	#PERSON PICKING-UP DONATION
	Persons= models.CharField(max_length=20, null=True)
	#CONTACT INFO
	Contact= models.IntegerField(null=True)
	#NUMBER OF BENEFICIARIES
	Beneficiaries= models.IntegerField(null=True)


	def __str__(self):
		return self.Receiver


