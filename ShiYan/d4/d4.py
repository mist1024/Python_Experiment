
import calendar

n_days = calendar.monthrange(2020, 10)   # 返回结果:(1, 30)
# calendar.monthrange(year,month)：第一个参数：指定月份第一天为周几（0-6 对应 周一 -周日）；第二个参数：指定月份的天数
print(n_days[1]) # 元组