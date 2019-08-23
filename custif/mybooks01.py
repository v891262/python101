#!/usr/bin/env python3
message = 'Based on your number rating, we recommend'

print('What is your value rating from 1 to 4?')
connection = float(input())
if connection== 1:
    message = message + ' Harry Potter'
elif connection== 2:
    message = message + ' Hobbit and the Lord of the Rings.'
elif connection== 3:
    message = message + ' Chronicles of Narnia.'
elif connection== 4:
    message = message + ' Indiana Jones.'
else:
    message = message + ' to watch Reading Rainbow to discover other magical books.'
print(message)
