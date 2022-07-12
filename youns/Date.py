from datetime import datetime
from dateutil.relativedelta import *

#날짜
today = datetime.today()
this_m = datetime.today().strftime('%Y-%m')
a_month_ago = datetime(today.year, today.month, today.day) + relativedelta(months=-1)
last_m = a_month_ago.strftime('%Y-%m')

last_mm = a_month_ago.strftime('%m')