#find difference between timestraps in UTC 
#datetime module

import datetime
def time_delta(t1,t2):
    string = "%a %d %b %Y %H:%M:%S %z" #format specifiers for date and time format
    T1=datetime.datetime.strptime(t1,string)
    T2=datetime.datetime.strptime(t2,string)
    return str(round(abs((T1-T2).total_seconds()))) #difference of timestraps