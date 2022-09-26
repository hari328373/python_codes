

#weekday using calender module
import calendar


def calen(month, day, year ):
    return calendar.day_name[calendar.weekday(year, month, day)].upper()

if __name__ == '__main__':
    month, day, year= int(input()),int(input()),int(input())
    calen(month, day, year)



