from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page

# Create your tests here.
class SmokeTest(TestCase):
	"""docstring for SmokeTest"""
	# def test_bad_maths(self):
		# self.assertEqual(1+1,3)
	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func,home_page)