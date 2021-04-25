from django.urls import resolve
from django.test import TestCase
from myWEB.views import Mainpage

from django.http import HttpRequest

class HomePageTest(TestCase):

	def test root_url_resolve_to_mainpage_view(self):
		found = resolve('/')
		self.assertEqual(found.func, MainPage)

	#def test_mainpage_return_correct_view(self):
		#request = HttpRequest()
		#response = MainPage(request)
		#html = response.content.decode('utf8')
		#self.assertTrue(html.startswitch('<html>'))
		#self.assertIn('<title>my WEB</title>', html)
		#self.assertTrue(html.endswitch('</html>'))

	'''def test_root_url_resolves_to_mainpage_view(self):
		found = resolve('/')
		self.assertEqual(found.func, Mainppage)

	#def test_mainpage_returns_correct_view(self):
		request = HttpRequest()
		response = Mainpage(request)
		html = response.content.decode('utf8')
		string_html = render_to_string('mainpage.html')
		self.assertEqual(html, string_html)

	def test_mainpage_returns_correct_view(self):
		request = HttpRequest()
		response = Mainpage(request)
		html = response.content.decode('utf8')
		self.assertTrue(html.strip().startswith('<html>'))
		self.assertIn('<title>'Balance Inquiry</title>', html)
		self.assertTrue(html.strip().endswith('</html>'))
		'''