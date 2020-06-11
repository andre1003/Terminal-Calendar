months = {
    1: ['January', 31],
    2: ['February', 20],
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
    1: {1, 'New Year'},
    2: {},
    3: {},
    4: {21, 'Tiradentes'},
    5: {1, "Labour Day"},
    6: {11, 'Corpus Christi'},
    7: {},
    8: {},
    9: {7, 'Independence Day'},
    10: {12, 'Lady of Aparecida'},
    11: {2: "All Souls' Day", 15: 'Republic Day'},
    12: {25, 'Christmas Day'}
}

def print_calendar(current_date):
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
    line = 1

    for i in range(1, days):
        holiday = False
        if line != 7:
            line+=1

        else:
            line = 1
            calendar += f'\n'

        for j in holidays[current_date.month]:
            if i == j:
                calendar += f' \033[7;33m{i:02d}\033[m '
                holiday = True
                break

        if i == current_date.day and holiday == False:
            calendar += f' \033[7m{i:02d}\033[m '
        elif holiday == False:
            calendar += f' {i:02d} '

        holiday = False

    calendar += '\n'
    print(calendar)