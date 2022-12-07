#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)
lastDigit = abs(number) % 10

if number >= 0:
        lastDigit = number % 10
else:
        lastDigit = -lastDigit
        output = f"Last digit of {number:d} is {lastDigit:d}"

        if lastDigit == 0:
                print(f"{output} and is 0")
        elif lastDigit > 5 and lastDigit % 10 != 0:
                print(f"{output} and is greater than 5")
        else:
                print(f"{output} and is less than 6 and not 0")
