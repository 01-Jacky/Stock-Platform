import datetime

date_string = '2018-01-15'
start_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
today = datetime.datetime.today()

time_delta_obj = today - start_date

print(time_delta_obj.days)


