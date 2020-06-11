# This is a terminal calendar made with python,
# so the idea is to keep it simple and workfull,
# but also user friendly

from datetime import datetime

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

print('Hello! Wellcome to Terminal Calendar!\n\n')

current_date = datetime.now()

days = months[current_date.month][1]

day = current_date.day
weekday = current_date.weekday()
while day > 1:
    day -= 1
    weekday -= 1
    if weekday == -1:
        weekday = 6
weekday += 1
print(' \033[31mS\033[m   M   T   W   T   F   \033[32mS\033[m', end="\n")

calendar = weekday*'    '
line = 1
for i in range(1, days):
    if line != 7:
        if i == current_date.day:
            calendar += f' \033[7m{i:02d}\033[m '
        else:
            calendar += f' {i:02d} '
        line+=1
    else:
        line = 1
        calendar += f'\n {i:02d} '
calendar += '\n'
print(calendar)

