import datetime

from django.test import TestCase
from hh.models import HappyHour
from hh.utils import get_day_of_week

h = HappyHour(name="Ashley's",notes='free beer',
	start_time='12:30 AM',
	end_time='3:00 AM',
	monday=True,
	tuesday=True,
	wednesday=True,
	thursday=False,
	friday=False,
	saturday=True,
	sunday=True,
	food=False,
	drink=True,
	city='Ann Arbor')

class HappyHourTestCase(TestCase):
	def create_happy_hour(self, name="Ashley's", notes='free beer',
							start_time='12:30 AM', end_time='3:00 AM',
							monday=True, tuesday=True, wednesday=True,
							thursday=False, friday=False, saturday=True,
							sunday=True, food=False, drink=True, city='Ann Arbor'
							):
		return HappyHour.objects.create(name=name, notes=notes,
							start_time=start_time, end_time=end_time,
							monday=monday, tuesday=tuesday, wednesday=wednesday,
							thursday=thursday, friday=friday, saturday=saturday,
							sunday=sunday, food=food, drink=drink, city=city)

	def test_whatever_creation(self):
		h = self.create_happy_hour()
		self.assertTrue(isinstance(h, HappyHour))
		self.assertEqual(h.avail_days(), ['M', 'Tu', 'W', 'Sa', 'Su'])

	def test_get_day_of_week(self):
		# TODO: how do you write a test when the result varies by time?
		self.assertEqual(get_day_of_week(datetime.datetime(2015, 9, 29, 20, 50, 12)), 'Tu')
