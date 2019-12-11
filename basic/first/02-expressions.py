#  Created by Artem Manchenkov
#  artyom@manchenkoff.me
#
#  Copyright © 2019
#
#  Условные и циклические конструкции языка
#

age = int(input("Your age: "))

if age > 14:
    print("You cant buy a ticket")
elif age == 14:
    print("All right")
else: 
    print("You can buy a ticket")


users = ["Artur", "John", "Jack"]

for user in users:
    print("Hello " + user)

counter = 0
while counter < 10:
    print(counter)
    counter += 1

