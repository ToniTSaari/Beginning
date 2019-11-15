import calendar, os
from time import gmtime, strftime


year = int( strftime ( '%Y', gmtime() ) )
month = int( strftime ( '%m', gmtime() ) )
date = int( strftime ( '%d', gmtime() ) )

day = calendar.weekday(year, month, date)
def backday():
    if day == 0:
        weekday = 'Maanantai'
    elif day == 1:
        weekday = 'Tiistai'
    elif day == 2:
        weekday = 'Keskiviikko'
    elif day == 3:
        weekday = 'Torstai'
    elif day == 4:
        weekday = 'Perjantai'
    elif day == 5:
        weekday = 'Lauantai'
    else:
        weekday = 'Sunnuntai'

    return weekday
