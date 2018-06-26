import datetime
import time


def get_this_month_head_timestamp():
    return round(int(datetime.datetime.today().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
                     .timestamp()))


def get_this_month_end_timestamp():
    global timestamp
    try:
        timestamp = datetime.datetime.today().replace(day=31, hour=23, minute=59, second=59, microsecond=0).timestamp()
    except ValueError:
        try:
            timestamp = datetime.datetime.today().replace(day=30, hour=23, minute=59, second=59, microsecond=0).timestamp()
        except ValueError:
            try:
                timestamp = datetime.datetime.today().replace(day=29, hour=23, minute=59, second=59, microsecond=0).timestamp()
            except ValueError:
                try:
                    timestamp = datetime.datetime.today().replace(day=28, hour=23, minute=59, second=59, microsecond=0).timestamp()
                except BaseException:
                    print('get timestamp error！')
    return round(int(timestamp))


def get_chinese_this_week_head_timestamp():
    now_weekday = datetime.datetime.now().weekday()
    now_day_head_timestamp = round(int(datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
                                       .timestamp()))
    return now_day_head_timestamp - 86400 * now_weekday


def get_chinese_this_week_end_timestamp():
    now_weekday = datetime.datetime.now().weekday()
    now_day_head_timestamp = round(int(datetime.datetime.today().replace(hour=23, minute=59, second=59, microsecond=0)
                                       .timestamp()))
    return now_day_head_timestamp + 86400 * (6 - now_weekday)


def get_this_week_head_timestamp():
    now_weekday = datetime.datetime.now().weekday()
    now_day_head_timestamp = round(int(datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
                                       .timestamp()))
    return now_day_head_timestamp - 86400 * (now_weekday + 1)


def get_this_week_end_timestamp():
    now_weekday = datetime.datetime.now().weekday()
    now_day_head_timestamp = round(int(datetime.datetime.today().replace(hour=23, minute=59, second=59, microsecond=0)
                                       .timestamp()))
    return now_day_head_timestamp + 86400 * (5 - now_weekday)


if __name__ == '__main__':
    print('this week week head:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(get_this_week_head_timestamp())))
    print('this week week end:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(get_this_week_end_timestamp())))
    print('this week week head(chinese):  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(get_chinese_this_week_head_timestamp())))
    print('this week week end(chinese):  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(get_chinese_this_week_end_timestamp())))
    print('this month month head:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(get_this_month_head_timestamp())))
    print('this month month end:  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(get_this_month_end_timestamp())))
