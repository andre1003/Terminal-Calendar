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
    3: 'Delete event',
    4: 'Import events (from an .txt file)',
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
    print()

    if choice == 1:
        new_event = calendar.add_event(current_date)
    
    elif choice == 2:
        calendar.print_events()
        input('\nType anything to continue...')

    elif choice == 3:
        calendar.delete_event()
        input('\nType anything to continue...')

    elif choice == 4:
        filename = input('Type the filename (without .txt): ')
        calendar.import_events(filename)
        print('File successfully imported!')
        input('\nType anything to continue...')
        
    elif choice == 0:
        clear()
        break
