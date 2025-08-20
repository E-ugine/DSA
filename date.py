from datetime import date, datetime , timedelta

today = date.today()
print(today)

#specific date
my_birthday = date(2025, 12,30)
print(my_birthday)

now = datetime.now()
print(now)
print(now.strftime("%A,%d %B %Y"))

tomorrow = today + timedelta(days=1)
print(tomorrow)