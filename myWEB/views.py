from django.shortcuts import redirect, render
from .models import Sponsor, Option, Monetary, Transaction, Inkind, Settlement, Fundraising, Recipient
# Create your views here.

def main(request):


	return render(request,'main.html')


def firstpage(request):



	return render(request,'firstpage.html')

def sponsor(request):

	viewer=Sponsor.objects.create(
		First = request.POST['First'],
		Surname = request.POST['Surname'],
		Email = request.POST['Email'],
		Contact = request.POST['Contact'],
		Address = request.POST['Address'],
		)

	return render(request,'fundraising.html')
	#return redirect('success')


def secondpage(request):

	# viewer1=Monetary.objects.create(
	# 	List = request.POST['List'],
	# 	Amount = request.POST['Amount'],
	# 	Gcash = request.POST['Gcash'],
	# 	Bank = request.POST['Bank'],
	# 	Bills = request.POST['Bills']
	# 	)

	# viewer2=Transaction.objects.create(
	# 	Place = request.POST['Place'],
	# 	Fee = request.POST['Fee'],
	# 	)

	# viewer3=Inkind.objects.create(
	#	Food = request.POST['Food'],
	# 	Drinks = request.POST['Drinks'],
	# 	Sanitation = request.POST['Sanitation'],
	# 	Cure = request.POST['Cure'],
	# 	Count = request.POST['Count'],
	# 	Count1 = request.POST['Couunt1'],
	# 	Count2 = request.POST['Count2'],
	# 	Count3 = request.POST['Count3'],
	# 	)

	# viewer4=Settlement.objects.create(
	# 	Locations = request.POST['Locations'],
	# 	Places = request.POST['Places'],
	# 	Charges = request.POST['Charges']
	# 	)

	viewer3=Inkind.objects.create(
		Food = request.POST['Food'],
		Drinks = request.POST['Drinks'],
		Sanitation = request.POST['Sanitation'],
		Cure = request.POST['Cure'],
		Count = request.POST['Quantity1'],
		Count1 = request.POST['Quantity2'],
		Count2 = request.POST['Quantity3'],
		Count3 = request.POST['Quantity4'],
		)


	viewer5=Fundraising.objects.create(
		Organization = request.POST['Group'],
		Organizer = request.POST['Organizer'],
		Event = request.POST['Activities'],
		Area = request.POST['Region'],
		Email = request.POST['Mails'],
		Time = request.POST['When'],
		Item = request.POST['Mass'],
		Sum = request.POST['Portion'],
		)


	return render(request,'recipient.html') 

def donation(request):

	viewer6=Recipient.objects.create(
		Receiver = request.POST['Receiver'],
		Dates = request.POST['Dates'],
		Persons = request.POST['Picker'],
		Contact = request.POST['Contacts'],
		chosen = request.POST['choose']


	
		)

	return render(request,'summary.html')




