from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from myWEB.views import Mainpage
from myWEB.views import Page
from django.urls import resolve
#For Models testing
#from myWEB.models import Item
from myWEB.models import Item, User 

'''
class NewListTest(TestCase):
	def test_uses_home_template(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'mainpage.html')
		

	def test_can_save_a_POST_request(self):
		self.client.post('/Donation/', data={'Donor': 'Eden P. Mendoza'})

		self.assertEqual(Item.objects.count(), 0)
		Donor = Item.objects.first()
		self.assertEqual(Donor.text, 'Eden P. Mendoza')

		self.client.post('/lists/new', data={'item_text': 'A new list item'})

		self.assertEqual(Item.objects.count(), 0)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text, 'A new list item')'''


class IndexTest(TestCase):

	def html_index_first(self):
		found = resolve('/')
		self.assertEqual(found.func, Mainpage)

		
	def test_index_returns_correct_view(self):
		request = HttpRequest()
		response = Mainpage(request)
		html = response.content.decode('UTF-8')
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'mainpage.html')

		self.assertTrue(html.strip().startswith('<html>'))
		self.assertTemplateUsed(response, 'mainpage.html')
		self.assertIn('<title>DONATION ENTRY</title>', html)

		self.assertTemplateUsed(response, 'mainpage.html')
		self.assertIn('<html>', html)
		self.assertIn('<head>', html)
		self.assertIn('<title>DONATION ENTRY</title>', html)
		self.assertIn('</head>', html)
		self.assertIn('<body style="background-color:#FFDEAD;">', html)
		self.assertIn('<center><h1 style="color:tomato; font-size:30px;">IN-KIND DONATION ENTRY</h1></center>', html)
		self.assertIn('<center><h1 style="color:black; font-style:oblique; font-size:17px;" id="me" >A Bayanihan for the Underprivileged</h1><br><br></center>', html)
		self.assertIn('<form class ="form" action="" method="post">', html)
		self.assertIn('<center>', html)
		self.assertIn('<input bold type="text" id="Donor" name="Donor" placeholder="Name of Donor" size="23">', html)
		self.assertIn('<input bold type="text" id="Email" name="Email" placeholder="Email Address" size="23">', html)
		self.assertIn('<br><br>', html)
		self.assertIn('<input bold type="text" id="Donation" name="Donation" placeholder="Item Donation" size="23">', html)
		self.assertIn('<input bold type="text" id="Items" name="Items" placeholder="Item Specifics: Volume and Packaging" size="23">', html)
		self.assertIn('<br><br>', html)
		self.assertIn('<div id="tion">', html)
		self.assertIn('<p style="font-style:oblique;">Type of Donation Support:</p>', html)
		self.assertIn('<input type ="radio" id="button1" name="tion" value="Personal Donation">Personal Donation<br>', html)
		self.assertIn('<input type ="radio" id="button2" name="tion" value="Company Donation">Company Donation<br><br>', html)
		self.assertIn('</div>', html)
		self.assertIn('<input bold type="text" id="Message" name="Message" placeholder="Special Instructions" size="23">', html)
		self.assertIn('<br><br>', html)
		self.assertIn('<input type="submit" name="submit" id="submit" value="Donate">', html)
		self.assertIn('</center>', html)
		self.assertIn('</form>', html)
		self.assertIn('</body>', html)
		self.assertIn('</form>', html)

		self.assertTrue(html.strip().endswith('</html>'))

class ORM_first(TestCase):
	def test_savings_(self):
		Item1 = Item()
		Item1.Donor = 'Eden P. Mendoza'
		Item1.save()
		Item2 = Item()
		Item2.Email = 'edenpino11@gmail.com'
		Item2.save()
		Item3 = Item()
		Item3.Donation = 'drinks'
		Item3.save()
		Item4 = Item()
		Item4.Items = '10L of water'
		Item4.save()
		Item5 = Item()
		Item5.tion = 'Personal Donation'
		Item5.save()
		Item6 = Item()
		Item6.Message = 'Handle with care'
		Item6.save()
		saveall = Item.objects.all()
		self.assertEqual(saveall.count(), 6)
		save1 = saveall[0]
		save2 = saveall[1]
		save3 = saveall[2]
		save4 = saveall[3]
		save5 = saveall[4]
		save5 = saveall[5]
		self.assertEqual(Item1.Donor, 'Eden P. Mendoza')
		self.assertEqual(Item2.Email, 'edenpino11@gmail.com')
		self.assertEqual(Item3.Donation, 'drinks')
		self.assertEqual(Item4.Items, '10L of water')
		self.assertEqual(Item5.tion, 'Personal Donation')
		self.assertEqual(Item6.Message, 'Handle with care')

class ORM_second(TestCase):
	def test_savings_(self):
		Item1 = Item()
		Item1.Donor = 'Ronan Kyle Ranido'
		Item1.save()
		Item2 = Item()
		Item2.Email = 'rronankyle@gmail.com'
		Item2.save()
		Item3 = Item()
		Item3.Donation = 'foods'
		Item3.save()
		Item4 = Item()
		Item4.Items = '15 sacks of rice'
		Item4.save()
		Item5 = Item()
		Item5.tion = 'Company Donation'
		Item5.save()
		Item6 = Item()
		Item6.Message = 'Enjoy it!'
		Item6.save()
		saveall = Item.objects.all()
		self.assertEqual(saveall.count(), 6)
		save1 = saveall[0]
		save2 = saveall[1]
		save3 = saveall[2]
		save4 = saveall[3]
		save5 = saveall[4]
		save5 = saveall[5]
		self.assertEqual(Item1.Donor, 'Ronan Kyle Ranido')
		self.assertEqual(Item2.Email, 'rronankyle@gmail.com')
		self.assertEqual(Item3.Donation, 'foods')
		self.assertEqual(Item4.Items, '15 sacks of rice')
		self.assertEqual(Item5.tion, 'Company Donation')
		self.assertEqual(Item6.Message, 'Enjoy it!')

class Views(TestCase):
	def test_joy(self):
		Item.objects.create(Donor='Donor', 
			Email='Email', Donation='Donation',
			Items='Items', tion='tion', Message='Message')
		response = self.client.get('/app/views.Mainpage/')


class ListViewTest(TestCase):

	def test_uses_list_template(self):
		viewer = User.objects.create()
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'mainpage.html')

	def test_uses_home_template(self):
		response = self.client.get('/donation/')
		#self.assertTemplateUsed(response, 'donation.html')

	def test_displays_all_list_items(self):
		viewer = User.objects.create()
		Donor = Item.objects.create(Donor='Donor')
		Email = Item.objects.create(Email='Email')
		Donation = Item.objects.create(Donation='Donation')
		Items = Item.objects.create(Items='Items')
		tion = Item.objects.create(tion='tion')
		Message = Item.objects.create(Message='Message')
		response = self.client.get('/')
		self.assertIn('Donor', response.content.decode())
		self.assertIn('Email', response.content.decode())
		self.assertIn('Donation', response.content.decode())
		self.assertIn('Items', response.content.decode())
		self.assertIn('tion', response.content.decode())
		self.assertIn('Message', response.content.decode())
		Donor = Item.objects.get(Donor="Donor")
		Email = Item.objects.get(Email="Email")
		Donation = Item.objects.get(Donation="Donation")
		Items = Item.objects.get(Items="Items")
		tion = Item.objects.get(tion="tion")
		Message = Item.objects.get(Message="Message")
		self.assertEqual(Item.objects.count(), 6)

		
class Views(TestCase):
	def setUp(self):
		Donor = Item.objects.create()
		Email = Item.objects.create()
		Donation = Item.objects.create()
		Items = Item.objects.create()
		tion = Item.objects.create()
		Message = Item.objects.create()
		
		Item.objects.create(
			Donor = 'Eden P. Mendoza',
			Email = 'edenpino11@gmail.com',
			Donation = 'drinks',
			Items = '10L of water',
			tion = 'Personal Donation',
			Message = 'Handle with care',
			)
		self.client.post('/donation/', name='Eden P. Mendoza')
		
		#response = 
		self.client.post('/donation/')

		self.assertEqual(Item.objects.count(), 7)
		#self.assertRedirects(response, '/next/')

	def test_redirect_view(self):
		Donor = Item.objects.get(Donor="Eden P. Mendoza")
		Email = Item.objects.get(Email="edenpino11@gmail.com")
		Donation = Item.objects.get(Donation="drinks")
		Items = Item.objects.get(Items="10L of water")
		tion = Item.objects.get(tion="Personal Donation")
		Message = Item.objects.get(Message="Handle with care")

		#response = self.client.post('/next/')
		#self.assertRedirects(response, '/donation/')

class Models(TestCase):

	def model(self, 
		Donor="test1", 
		Email="test2", 
		Donation="test3", 
		Items="test4", 
		tion="test5", 
		Message="test6", 
		):
		
		return User.objects.create()
		return Item.objects.create(
			Donor="Donor", 
			Email="Email", 
			Donation="Donation", 
			Items="Items", 
			tion="tion", 
			Message="Message", 
			)

	def test_whatever_creation(self):
		w = self.modelo()
		self.assertTrue(isinstance(w, User))
		self.assertFalse(isinstance(w, Item))
