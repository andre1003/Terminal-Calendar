# This is a terminal calendar made with python,
# so the idea is to keep it simple and workfull,
# but also user friendly

from datetime import datetime
import calendar
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

options = {
    1: 'Add new event',
    2: 'Show events',
    0: 'Exit'
}

new_event = False


while True:
    clear()
    if new_event:
        print('Event saved successfully!')
        new_event = False

    print('Hello! Wellcome to Terminal Calendar!\n\n')

    current_date = datetime.now()

    calendar.print_calendar(current_date)

    for op in options:
        print(f'{op} - {options[op]}')

    choice = int(input('What do you want to do? '))

    if choice == 1:
        new_event = calendar.add_event(current_date)
    
    elif choice == 2:
        calendar.print_dates()
        input('Type anything to continue...')
        
    elif choice == 0:
        clear()
        break
