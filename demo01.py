import calendar

# 获取当前年份和月份
year = int(input("请输入要查询的年份（如2021）："))
month = int(input("请输入要查询的月份（如9表示九月）："))

# 生成指定年份、月份的日历
cal = calendar.month(year, month)
print(f"{year}年{month}月的日历:\n")
print(cal)