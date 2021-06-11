from django.shortcuts import redirect, render
from .models import Sponsor, Option, Monetary, Transaction, Inkind, Settlement, Fundraising, Recipient
# Create your views here.


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

	return render(request,'donor.html')
	return redirect('success')


'''def option(request):

	viewer=Option.objects.create(
		choose = request.POST[('Monetary Donation', 'Monetary Donation'), ('In-Kind Donation', 'In-Kind Donation')],
		#Donors = request.POST['Donors'],
		Message = request.POST['Message'],
		)

	return render(request,'donor.html')
	return redirect('success')'''






