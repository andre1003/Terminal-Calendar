# Static variables
months = {
    1: ['January', 31],
    2: ['February', 28],
    3: ['March', 31],
    4: ['April', 30],
    5: ['May', 31],
    6: ['June', 30],
    7: ['July', 31],
    8: ['August', 31],
    9: ['September', 30],
    10: ['October', 31],
    11: ['November', 30],
    12: ['December', 31]
}

holidays = {
    1: {1: 'New Year'},
    2: {},
    3: {},
    4: {21: 'Tiradentes'},
    5: {1: "Labour Day"},
    6: {11: 'Corpus Christi'},
    7: {},
    8: {},
    9: {7: 'Independence Day'},
    10: {12: 'Lady of Aparecida'},
    11: {2: "All Souls' Day", 15: 'Republic Day'},
    12: {25: 'Christmas Day'}
}


def print_calendar(current_date):
    '''
    :Params:
        current_date
    
    :Return:
        Nothing

    :Description:
        This functions prints the calendar on terminal,
        marking the current day, events and holidays.
    '''

    days = months[current_date.month][1]

    day = current_date.day
    weekday = current_date.weekday()
    while day > 1:
        day -= 1
        weekday -= 1
        if weekday == -1:
            weekday = 6
    weekday += 1

    month = months[current_date.month][0]
    spaces = int((26 - len(month)) / 2)
    string = spaces*' '
    string += f' \033[7m{month}\033[m '
    string += spaces*' '
    print(string)

    print(' \033[31mS\033[m   M   T   W   T   F   \033[32mS\033[m')

    calendar = weekday*'    '
    comment = ''
    line = 1

    events = get_events(current_date.month, current_date.year)

    has_holiday = False
    for i in range(1, days + 1):
        holiday = False
        if line != 7:
            line+=1

        else:
            line = 1
            calendar += f'\n'

        for j in holidays[current_date.month]:
            if i == j and i != current_date.day:
                calendar += f' \033[7;33m{i:02d}\033[m '
                holiday = True
                has_holiday = True
                break

        if events:
            for j in events:
                if i == j and i != current_date.day:
                    calendar += f' \033[7;36m{i:02d}\033[m '
                    holiday = True
                    break
                elif i == j:
                    comment = 'Today is an event day!'

        if i == current_date.day and holiday == False:
            calendar += f' \033[7m{i:02d}\033[m '
        elif holiday == False:
            calendar += f' {i:02d} '

        holiday = False

    print(calendar + '\n')

    if has_holiday:
        print('Holiday(s):')
        aux = holidays[current_date.month]
        for i in aux:
            print(f'Day {i} - {aux[i]}')

        print()

    if comment:
        print(comment + '\n')


def get_events(current_month, current_year):
    '''
    :Params:
        current_month, current_year

    :Return:
        List of events or None

    :Description:
        This function gets all events of current month from the
        events file. If no event was found, return None.
    '''

    try:
        file = open('events.txt', 'r')
        content = file.readlines()
        
        file.close()

        events = list()
        for item in content:
            item = item.replace('\n', '')
            
            item = item.split('/')
            item = list(map(int, item))
            if item[2] == current_year:
                
                if item[1] == current_month:
                    events.append(item[0])

        return events

    except:
        return None


def file_insertion(filename, data):
    '''
    :Params:
        filename, data

    :Return:
        Nothing

    :Description:
        This function insert some data on an specific file.
    '''

    try:
        file = open(filename, 'r')
        content = file.readlines()
        
        content.append(data)
        file = open(filename, 'w')
        file.writelines(content)

        file.close()

    except:
        file = open(filename, 'w')
        file.write(data)
        file.close()


def insert_db(date, description):
    '''
    :Params:
        date, description

    :Return:
        Nothing

    :Description:
        This function prepare event data to be inserted on
        respective file.
    '''

    date += '\n'
    description += '\n'
    file_insertion('events.txt', date)
    file_insertion('descriptions.txt', description)


def add_event(current_date):
    '''
    :Params:
        current_date

    :Return:
        True or False

    :Description:
        This function add a new event, making the respective validations
        and return True if event is successfully inserted in file or False
        if operations has been canceled.
    '''

    while True:
        date = input("Insert the event's date (dd/mm/yyyy) (type 'c' to go back to menu): ")
        if date == 'c':
            return False

        event = validate_date(date, current_date)
        if not event:
            print('Invalid date! Try again, please.')

        else:
            description = input('Type a description for this event: ')
            confirm = input(f'The date is {event[0]:02d}/{event[1]:02d}/{event[2]:04d}? [y/n] (y): ')

            if confirm == 'y' or not confirm:
                # Date confirmed
                insert_db(f'{event[0]}/{event[1]}/{event[2]}', description)
                return True


def delete_event():
    '''
    :Params:
        Nothing

    :Return:
        Nothing

    :Description:
        This function show the options for deletion and remove
        what user chose.
    '''

    try:
        file = open('events.txt', 'r')
        dates = file.readlines()
        file.close()

        file = open('descriptions.txt', 'r')
        descriptions = file.readlines()
        file.close()
        
        i = 1
        for item in dates:
            print(f'{i} - {item}')
            i+=1

        op = int(input('Which event you want to delete? '))

        while op > len(dates) or op <= 0:
            op = int(input('Invalid option, try again: '))

        
        del(dates[op-1])
        del(descriptions[op-1])

        file = open('events.txt', 'w')
        file.writelines(dates)
        file.close()

        file = open('descriptions.txt', 'w')
        file.writelines(descriptions)
        file.close()

        print('Event successfully deleted!')

    except:
        print('Something wrong happened with events file :/')


def validate_date(date, current_date):
    '''
    :Params:
        date, current_date

    :Return:
        List with date (splitted) or None

    :Description:
        This function makes date validation, returning a list splitted by [day, month, year]
        or None, if date is invalid.
    '''

    date = date.split('/')
    if len(date) != 3:
        return None

    try:
        day = int(date[0])
        month = int(date[1])
        year = int(date[2])

    except:
        return None

    if year >= current_date.year + 60 or month < 1 or month > 12 or day < 1 or day > months[month][1]:
        return None

    if year < current_date.year:
        return None
    elif year > current_date.year:
        return [day, month, year]
    else:
        if month < current_date.month:
            return None
        elif month > current_date.month:
            return [day, month, year]
        else:
            if day <= current_date.day:
                return None
            elif day > current_date.day:
                return [day, month, year]


def import_events(filename):
    '''
    :Params:
        filename

    :Return:
        Nothing

    :Description:
        This function import an event file to configuration file.
    '''

    filename += '.txt'
    try:
        file = open(filename, 'r')
        file.close()

        config = open('config.cfg', 'r')
        content = config.readlines()

        content.append(filename + '\n')
        config = open('config.cfg', 'w')
        config.writelines(content)

        config.close()

    except:
        print("The file doesn't exist!")


def print_events():
    '''
    :Params:
        Nothing

    :Return:
        Nothing

    :Description:
        This function get all events and print then on screen.
    '''

    try:
        date = open('events.txt', 'r')
        dates = date.readlines()
        date.close()

        description = open('descriptions.txt', 'r')
        descriptions = description.readlines()
        description.close()
        
        end = len(dates)
        for i in range(0, end):
            dates[i] = dates[i].replace('\n', '')
            print(f'{dates[i]} - {descriptions[i]}')

        
    except:
        print('There is no event saved yet :/')


from dateutil.relativedelta import *
from datetime import datetime

# use_date = datetime.now()
# print(f'This month weekday (today): {use_date.weekday()}')

# use_date = use_date+relativedelta(months=+1)
# use_date = use_date+relativedelta(day=1)

# print(f'Next month weekday (today): {use_date.weekday()}')
def calculate_date(option):
    if option == 1:
        date = datetime.now()
        date = date + relativedelta(months=+1)
        date = date + relativedelta(day=1)
        print_calendar(date)

    else:
        pass


def OnKeyPress(event):
    if event.Key == 'Left':
        calculate_date(1)
            

import pyxhook
def navigate():
    hm = pyxhook.HookManager()
    hm.KeyDown = OnKeyPress

    hm.HookKeyboard()

    hm.start()