from dateutil import rrule
from dateutil.parser import parse
from dateutil.relativedelta import *
import datetime

#Input 起始时间，结束时间，每天上班时间（9），每天下班时间（17）
def workhours(start, end, timeon, timeoff, days_off=None):
    #Correct Format
    start = parse(start)
    end = parse(end)

    if days_off is None:
        dailyList = list(rrule.rrule(rrule.DAILY, byweekday=(MO, TU, WE,TH, FR), dtstart=start, until=end))
        days = len(dailyList)

        #节假日
        for date in dailyList:
            #元旦
            if date.month == 1 and date.day == 1:
                days = days - 1
            #春节
            elif date.month == 2 and date.day == 8:
                days = days - 5
            #清明
            elif date.month == 4 and date.day == 4:
                days = days - 1
            #劳动节
            elif date.month == 5 and date.day == 2:
                days = days - 1
            #端午节
            elif date.month == 6 and date.day == 9:
                days = days - 2
            #中秋节
            elif date.month == 9 and date.day == 15:
                days = days - 2
            #国庆节
            elif date.month == 10 and date.day == 3:
                days = days - 5

        #First day and last day
        trimstart = (start.hour) - timeon
        trimend = timeoff - end.hour

        totalhours = (days)*(timeoff-timeon) - trimstart - trimend

        return totalhours

# workhours(datetime.datetime(2016, 6, 8, 9, 35), datetime.datetime(2016, 6, 13, 15, 36), 9, 17)
print("Working Hours: " + str(workhours("2016-2-1 10:15", "2016-2-19 17:00", 9, 17)))