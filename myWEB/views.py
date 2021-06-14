from django.shortcuts import redirect, render
from .models import Sponsor, Option, Monetary, Transaction, Inkind, Settlement, Fundraising, Recipient
# Create your views here.

def main(request):

	return render(request,'main.html')


def firstpage(request):

	return render(request,'firstpage.html')

def sponsor(request):

	'''viewer=Sponsor.objects.create(
		First = request.POST['First'],
		Surname = request.POST['Surname'],
		Email = request.POST['Email'],
		Contact = request.POST['Contact'],
		Address = request.POST['Address'],
		)'''

	return render(request,'donationtype.html')
	#return redirect('success')


def secondpage(request):

	return render(request,'fundraising.html') 

def donation(request):

	return render(request,'recipient.html')

# def option(request):

# 	'''viewer=Option.objects.create(
# 		choose = request.POST[('Monetary Donation', 'Monetary Donation'), ('In-Kind Donation', 'In-Kind Donation') ('Both', 'Both')],
# 		#Donors = request.POST['Donors'],

# 		)'''

# 	return render(request,'fundraising.html')
# 	#return redirect('success')

# def monetary(request):

# 	'''viewer=Sponsor.objects.create(
# 		First = request.POST['First'],
# 		Surname = request.POST['Surname'],
# 		Email = request.POST['Email'],
# 		Contact = request.POST['Contact'],
# 		Address = request.POST['Address'],
# 		)'''

# 	return render(request,'donationtype.html')
# 	#return redirect('success')


# def transaction(request):

# 	'''viewer=Sponsor.objects.create(
# 		First = request.POST['First'],
# 		Surname = request.POST['Surname'],
# 		Email = request.POST['Email'],
# 		Contact = request.POST['Contact'],
# 		Address = request.POST['Address'],
# 		)'''

# 	return render(request,'donationtype.html')
# 	#return redirect('success')


# def inkind(request):

# 	'''viewer=Sponsor.objects.create(
# 		First = request.POST['First'],
# 		Surname = request.POST['Surname'],
# 		Email = request.POST['Email'],
# 		Contact = request.POST['Contact'],
# 		Address = request.POST['Address'],
# 		)'''

# 	return render(request,'donationtype.html')
# 	#return redirect('success')

# def settlement(request):

# 	'''viewer=Sponsor.objects.create(
# 		First = request.POST['First'],
# 		Surname = request.POST['Surname'],
# 		Email = request.POST['Email'],
# 		Contact = request.POST['Contact'],
# 		Address = request.POST['Address'],
# 		)'''

# 	return render(request,'donationtype.html')
# 	#return redirect('success')'''

def fundraising(request):

	'''viewer=Sponsor.objects.create(
		First = request.POST['First'],
		Surname = request.POST['Surname'],
		Email = request.POST['Email'],
		Contact = request.POST['Contact'],
		Address = request.POST['Address'],
		)'''

	return render(request,'fundraising.html')
	#return redirect('success')

def recipient(request):

	'''viewer=Sponsor.objects.create(
		First = request.POST['First'],
		Surname = request.POST['Surname'],
		Email = request.POST['Email'],
		Contact = request.POST['Contact'],
		Address = request.POST['Address'],
		)'''

	return render(request,'recipient.html')
	#return redirect('success')






