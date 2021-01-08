'''
输入某年某月某日,判断这一天是这一年的第几天？
'''


def is_leap_year(year):
    # if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    #     return True
    # else:
    #     return False
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def get_day_by_month(year, month):
    if 1 <= month <= 12:
        if month == 2:
            return 29 if is_leap_year(year) else 28
        if month in (4, 6, 9, 11):
            return 30
        return 31


print(get_day_by_month(2020, 2))
