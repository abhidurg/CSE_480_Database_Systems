import datetime
def alarm_rings(start_date_ISO, end_date_ISO):
    start_date = datetime.datetime.strptime(start_date_ISO, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date_ISO, "%Y-%m-%d")
    diff = datetime.timedelta(days=1)
    result_list = []
    while start_date <= end_date:
        if start_date.weekday() < 5:
            result_list.append(start_date.replace(hour=7).strftime("%Y-%m-%d %H:%M:%S"))
        else:
            result_list.append(start_date.replace(hour=9).strftime("%Y-%m-%d %H:%M:%S"))
        start_date += diff
    return result_list