from django.shortcuts import redirect, render
from .models import Item, User
# Create your views here.
def Mainpage(request):
	
	if request.method == 'POST':


		kind=User.objects.create()
		Item.objects.create(
			Donor = request.POST['Donor'],
			Email = request.POST['Email'],
			Donation = request.POST['Donation'],
			Items = request.POST['Items'],
			tion = request.POST['tion'],
			Message = request.POST['Message'],
			)
		return redirect('donation')


		#Donor = request.POST['Donor']
		#Email = request.POST['Email']
		#Donation = request.POST['Donation']
		#Items = request.POST['Items']
		#tion = request.POST['tion']
		#Message = request.POST['Message']
		
		jnd = Item()
		jnd.Donor = Donor
		jnd.Email = Email
		jnd.Donation = Donation
		jnd.Items = Items
		jnd.tion = tion
		jnd.Message = Message
		jnd.save()

	return render(request,'mainpage.html')

def Page (request):
	#return render(request,'donation.html')

	jnd = Item.objects.all().order_by('Donor')
	return render(request,'donation.html', {'jnd': jnd})



