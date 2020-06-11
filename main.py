# This is a terminal calendar made with python,
# so the idea is to keep it simple and workfull,
# but also user friendly

from datetime import datetime
import calendar
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


clear()
print('Hello! Wellcome to Terminal Calendar!\n\n')

current_date = datetime.now()

calendar.print_calendar(current_date)