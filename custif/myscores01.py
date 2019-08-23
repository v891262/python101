
#!/usr/bin/env python3
message = 'Based on your letter grade, you fall between'

print('What is your letter grade?')
connection = input()
if connection == "A":
    message = message + ' (90 to 100)'
elif connection== "B":
    message = message + ' (80 to 89).'
elif connection=="C":
    message = message + ' (70 to 79)'
elif connection=="D":
    message = message + ' (60 to 69)'
elif connection=="F":
    message = message + ' (59 and below)'
else:
    message = message + 'You did not put in a valid grade Please run the program again and enter a valid grade.'
print(message)

