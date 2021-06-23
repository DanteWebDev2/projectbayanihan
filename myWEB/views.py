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

	return render(request,'donationtype.html')
	#return redirect('success')


def secondpage(request):

	viewer=Monetary.objects.create(
		List = request.POST['List'],
		Amount = request.POST['Amount'],
		Gcash = request.POST['Gcash'],
		Bank = request.POST['Bank'],
		Bills = request.POST['Bills'],
		)

	viewer=Transaction.objects.create(
		Place = request.POST['Place'],
		Fee = request.POST['Fee'],
		)

	viewer=Inkind.objects.create(
		Food = request.POST['Food'],
		Drinks = request.POST['Drinks'],
		Sanitation = request.POST['Sanitation'],
		Cure = request.POST['Cure'],
		Count = request.POST['Count'],
		Count1 = request.POST['Couunt1'],
		Count2 = request.POST['Count2'],
		Count3 = request.POST['Count3'],
		)

	viewer=Settlement.objects.create(
		Locations = request.POST['Locations'],
		Places = request.POST['Places'],
		Charges = request.POST['Charges'],
		)

	return render(request,'fundraising.html') 

def donation(request):

	viewer=Fundraising.objects.create(
		Organization = request.POST['Organization'],
		Organizer = request.POST['Organizer'],
		Event = request.POST['Event'],
		Area = request.POST['Area'],
		Email = request.POST['Email'],
		Time = request.POST['Time'],
		Item = request.POST['Item'],
		Sum = request.POST['Sum'],
		)

	return render(request,'recipient.html')

def donates(request):

	viewer=Recipient.objects.create(
		Receiver = request.POST['Receiver'],
		Dates = request.POST['Dates'],
		Persons = request.POST['Person'],
		Contact = request.POST['Contact'],
		Beneficiaries = request.POST['Beneficiaries'],
	
		)

	return render(request,'summary.html')







