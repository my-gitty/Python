# ----------------------- calendar ----------------------- #

import calendar
# judging whether the year is leap year or not
print( calendar.isleap(1900))
print( calendar.isleap(2000))

# ----------------------- calendar ----------------------- #

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# ----------------------- datetime ----------------------- #

from datetime import date

# hallowee day
hallowee = date(2014, 10, 31)
print(hallowee)
print(hallowee.day)
print(hallowee.month)
print(hallowee.year)

# ISO format
print(hallowee.isoformat())

# today
now = date.today()
print(now)

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

from datetime import timedelta
one_day = timedelta(days = 1)

# tomorrow
tomorrow = now + one_day
print(tomorrow)

# yesterday
yesterday = now - one_day
print(yesterday)

# other examples
print(now + 17*one_day)

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

from datetime import time

#time noon
noon = time(12, 0, 0)
print(noon)
print(noon.hour)
print(noon.second)
print(noon.microsecond)

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

from datetime import datetime
some_day = datetime(2014, 1, 2, 3, 4, 5, 6)
print(some_day)
print(some_day.isoformat())

now = datetime.now()
print(now)
print(now.hour)
print(now.second)
print(now.microsecond)

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

noon_today = datetime.combine(now, noon)
print(noon_today)
print(noon_today.date())
print(noon_today.time())

# ----------------------- datetime ----------------------- #


import time

now = time.time()
print(now)
print(time.ctime(now))
# return the current time
print(time.localtime(now))
# return the UTC time
print(time.gmtime(now))

# the time has difference with the privious 
# because the time just can express to second
tm = time.localtime(now)
print(time.mktime(tm))


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
print(
"""
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
"""
)
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# transform the localtime struct to the format
fmt = "It's %A, %B %d, %Y, local time %I:%M:%S%p"
t = time.localtime()
print(time.strftime(fmt,t))

# transform the time to the time struct
fmt = '%Y-%m-%d'
print(time.strptime('2016-2-5',fmt))

 
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
import locale
#from datetime import date
names = locale.locale_alias.keys()
good_names = [name for name in names if \
		      len(name) ==5 and name[2] == '_']
print(good_names[:5])

try:
	for lang_country in good_names[:5]:
		locale.setlocale(locale.LC_TIME, lang_country)
		print(hallowee.strftime("%A, %B %d"))
except:
	print('may has no permission')

