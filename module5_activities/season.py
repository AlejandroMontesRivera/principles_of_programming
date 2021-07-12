import calendar
import datetime

input_month = input()
input_day = int(input())

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']
spring = ['April', 'May', 'June']
summer = ['July', 'August', 'September']
fall = ['October', 'November']
winter = ['January', 'February', 'March']

if input_month in months and 31 > input_day > 0:
    if input_month in spring:
        season = 'Spring'
    elif input_month in summer:
        season = 'Summer'
    elif input_month in fall:
        season = 'Autumn'
    elif input_month in winter:
        season = 'Winter'
    elif (input_month == 'March') and (input_day > 19):
        season = 'Spring'
    elif (input_month == 'June') and (input_day > 20):
        season = 'Summer'
    elif (input_month == 'September') and (input_day > 21):
        season = 'Autumn'
    elif (input_month == 'December') and (input_day > 20):
        season = 'Winter'
    print(season)
else:
    print('Invalid')
