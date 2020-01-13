#
# Example file for working with Calendars
#

# import the calendar module
import calendar

# create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
# st = c.formatmonth(2019, 12, 0, 0) # "formatmonth" method allow format a particular month into a text string
# print(st)

# create an HTML formatted calendar
# hc = calendar.HTMLCalendar(calendar.SUNDAY)
# st = hc.formatmonth(2019,12)
# print(st)

# loop over the days of a month
# zeros mean that the day of the week is in an overlapping month
# for i in c.itermonthdays(2019, 12):
# 	print(i) # zeros at start and end, are the days that belongs to another month
  

# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
# for name in calendar.month_name:
# 	print(name)


# for day in calendar.day_name:
# 	print(day)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
  
print("Team meeting will be on: ")
for m in range(1,13): # loop over all the months
	# Get and array of weeks that represent each one of the months
	cal= calendar.monthcalendar(2019, m) # Specify year, m = month number 
	# create variables that represent week one and week two where the first FRIDAY will fall into
	weekone = cal[0]
	weektwo = cal[1]

	# let's check if the first FRIDAY falls into the first week of the month or in the second week
	if weekone[calendar.FRIDAY]	 != 0: # if the first FRIDAY = zero, it means that that Friday belongs to another month
		meetday = weekone[calendar.FRIDAY]

	else:
		meetday = weektwo[calendar.FRIDAY]

	print('%10s %2d' % (calendar.month_name[m], meetday))