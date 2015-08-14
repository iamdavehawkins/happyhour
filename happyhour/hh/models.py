from django.db import models
import datetime as dt

TIME_CHOICES = []
for h in range(0, 23):
	for m in [0, 30]:
		time_opt = dt.time(h, m)
		TIME_CHOICES.append((time_opt, time_opt.strftime('%-I:%M %p')))

class HappyHour(models.Model):
	# TODO: add User ForeignKey field and migrate db (also update forms.py and views.py)
	name = models.CharField(max_length=200)
	notes = models.CharField(max_length=200)
	start_time = models.TimeField('start time', choices=TIME_CHOICES)
	end_time = models.TimeField('end time', choices=TIME_CHOICES)
	monday = models.BooleanField(default=False)
	tuesday = models.BooleanField(default=False)
	wednesday = models.BooleanField(default=False)
	thursday = models.BooleanField(default=False)
	friday = models.BooleanField(default=False)
	sunday = models.BooleanField(default=False)
	saturday = models.BooleanField(default=False)
	food = models.BooleanField(default=False)
	drink = models.BooleanField(default=False)
	city = models.CharField(max_length=200)

	def __str__(self):
		return "a happy hour at {} from {} to {} on: {}".format(self.name, self.start_time, self.end_time,
											   ', '.join(self.avail_days())
											   )

	def avail_days(self):
		self.days = [self.monday, self.tuesday, self.wednesday, self.thursday,
				     self.friday, self.saturday, self.sunday]

		self.avail_days = []
		if self.monday:
			self.avail_days.append('M')
		if self.tuesday:
			self.avail_days.append('Tu')
		if self.wednesday:
			self.avail_days.append('W')
		if self.thursday:
			self.avail_days.append('Th')
		if self.friday:
			self.avail_days.append('F')
		if self.saturday:
			self.avail_days.append('Sa')
		if self.sunday:
			self.avail_days.append('Su')
		return self.avail_days