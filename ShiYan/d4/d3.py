import datetime
# 获取当前时间
today = datetime.datetime.now()
# 计算偏移量
offset = datetime.timedelta(days=-5)
# 获取想要的日期的时间
re_date = (today + offset).strftime('%Y-%m-%d')
print(today)
print(re_date)