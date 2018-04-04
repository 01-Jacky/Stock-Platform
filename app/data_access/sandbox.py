from datetime import datetime

date_string = '2018-03-24'
date1 = datetime.strptime(date_string, "%Y-%m-%d")

date_string = '2018-03-23'
date2 = datetime.strptime(date_string, "%Y-%m-%d")

date_delta = date2 - date1

print(date_delta.days)