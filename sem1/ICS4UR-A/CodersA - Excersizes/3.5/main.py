"""
Exercise 3.5 You look at the clock and see that it is currently 14.00h. You set an alarm to
go off 535 hours later. At what time will the alarm go off? Write a program that prints the
answer. Hint: for the best solution, you will need the modulo operator.


"""

# Current time in hours
current_time = 14

# Hours to add
hours_to_add = 535

# Calculate the time after adding hours and handle rollover
alarm_time = (current_time + hours_to_add) % 24

# Print the result
print(f"The alarm will go off at {alarm_time:02}.00h")



