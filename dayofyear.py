from datetime import datetime

usr_date = input("Enter date. (e.g. mm-dd-yyyy)")
print(usr_date)

format_date = "%m-%d-%Y"

datetime_object = datetime.strptime(usr_date, format_date)

day_of_the_Year = datetime_object.strftime('%j')

doy_int = int(day_of_the_Year)

print(f"The date {datetime_object.date()} is day {doy_int} of the year.")



up_to_inputdate =  
