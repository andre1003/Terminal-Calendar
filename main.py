# This is a terminal calendar made with python,
# so the idea is to keep it simple and workfull,
# but also user friendly
'''
    Imports
'''
from datetime import datetime
import functions
import os
import sys

'''
    Static variables
'''
options = {
    1: 'Add new event',
    2: 'Show events',
    3: 'Delete event',
    4: 'Import events (from an .txt file)',
    5: 'Navigate',
    0: 'Exit'
}

'''
    Global variables
'''
new_event = False

'''
    Functions
'''
def clear():
    '''
    :Params:
        Nothing

    :Return:
        Nothing
    
    :Description:
        This function clear the terminal
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


clear()
print('Hello! Wellcome to Terminal Calendar!\n\n')

while True:
    
    if new_event:
        print('Event saved successfully!')
        new_event = False

    current_date = datetime.now()

    functions.print_calendar(current_date)

    for op in options:
        print(f'{op} - {options[op]}')

    choice = int(input('What do you want to do? '))
    print()

    if choice == 1:
        clear()
        new_event = functions.add_event(current_date)
    
    elif choice == 2:
        functions.print_events()
        input('\nType anything to continue...')

    elif choice == 3:
        clear()
        functions.delete_event()
        input('\nType anything to continue...')

    elif choice == 4:
        clear()
        filename = input('Type the filename (without .txt): ')
        functions.import_events(filename)
        input('\nType anything to continue...')

    elif choice == 5:
        clear()
        functions.navigate()
        input('\nType anything to continue...')
        
    elif choice == 0:
        clear()
        break

    clear()
