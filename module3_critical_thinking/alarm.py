# Option #1: Alarm Time
# Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight).
# If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm).
# Write a Python program to solve the general version of the above problem. Ask the user for
# the time now (in hours) and then ask for the number of hours to wait for the alarm.
# Your program should output what the time will be on a 24-hour clock when the alarm goes off.

# Compile and submit your source code and screenshots of the application executing the code and
# the results in a single document.

current_time = int(input('What is the current time in hours (24h format)? '))
time_to_wait = int(input('Enter the number of hours to wait for the alarm: '))
tempTime = current_time + time_to_wait
time = tempTime % 24 if (tempTime > 24) else tempTime
print(f"In {time_to_wait}h it will be {time}h, ({time % 12} {'am' if time < 12 else 'pm'})")
