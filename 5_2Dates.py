#If we ever wat our user to insert a date, we can do the following
from datetime import datetime as dt, timedelta
today = dt.now()
birthday = input("Inserta tu fecha de compleaños dd/mm/yyyy: ")
dateBirthay = dt.strptime(birthday, "%d/%m/%Y")
difference = today-dateBirthay
print("Your birthday was: " + str(difference.days) +" days ago")

