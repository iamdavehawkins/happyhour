import datetime

def get_day_of_week(curr_datetime):
	week_day_map = {0 : 'M',
					1 : 'Tu',
					2 : 'W',
					3 : 'Th',
					4 : 'F',
					5 : 'Sa',
					6 : 'Su'}
	day_of_week = curr_datetime.weekday()
	hour = curr_datetime.time().hour

	if hour < 6:
		# if it's after midnight, return the previous day
		if day_of_week == 0:
			day_of_week = 6
		else:
			day_of_week = day_of_week - 1

	return week_day_map[day_of_week]
