#
# Example file for formatting time and date output
#

from datetime import datetime

def main():
  # Times and dates can be formatted using a set of predefined string
  # control codes 
	now = datetime.now()

  #### Date Formatting ####
  
  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
	# print(now.strftime("The current year is: %Y" ))
	# print(now.strftime("%a, %d, %B, %Y"))

  # %c - locale's date and time, %x - locale's date, %X - locale's time
	# print(now.strftime("local day and time: %c")) # print day, month, time, year  format
	# print(now.strftime("local day and time: %x")) # print month/day/year format
	# print(now.strftime("local day and time: %X")) # print time
  #### Time Formatting ####
  
  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
	print(now.strftime("current time: %I:%M:%S %p"))
	print(now.strftime("24-hrs time: %H:%M"))

if __name__ == "__main__":
  main();
