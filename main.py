@@ -1,134 +1,98 @@
# Calculator
import os
import time


def addition():

    print("Addition")

    n = float(input("Enter the number: "))

    t = 0  # Total number enter

    ans = 0

    while n != 0:

        ans = ans + n

        t += 1

        n = float(input("Enter another number (0 to calculate): "))

        return [ans, t]
    nums = list(
        map(int, input("Enter all numbers seperated by space: ").split()))
    return sum(nums)


def subtraction():

    print("Subtraction")

    n = float(input("Enter the number: "))

    t = 0  # Total number enter

    sum = 0

    while n != 0:

        ans = ans - n

        t += 1

        n = float(input("Enter another number (0 to calculate): "))
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))

        return [ans, t]
    return n1 - n2


def multiplication():
    nums = list(
        map(int, input("Enter all numbers seperated by space: ").split()))
    res = 1
    for num in nums:
        res *= num
    return res


def division():
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))

    return n1/n2


def average():
    nums = list(
        map(int, input("Enter all numbers seperated by space: ").split()))
    return sum(nums)/len(nums)


c = 0
while c != "-1":

    print("Enter '1' for addition")
    print("Enter '2' for subtraction")
    print("Enter '3' for multiplication")
    print("Enter '4' for division")
    print("Enter '5' for average")
    print("Enter '-1' to exit.\n")

    c = input("Your choice is: ")

    if c == "1":
        res = addition()
        os.system('cls')
        print(f"The answer is {res}")
        time.sleep(2)
        os.system('cls')

    elif c == "2":
        res = subtraction()
        os.system('cls')
        print(f"The answer is {res}")
        time.sleep(2)
        os.system('cls')

    elif c == "3":
        res = multiplication()
        os.system('cls')
        print(f"The answer is {res}")
        time.sleep(2)
        os.system('cls')

    elif c == "4":
        res = division()
        os.system('cls')
        print(f"The answer is {res}")
        time.sleep(2)
        os.system('cls')

    elif c == "5":
        res = average()
        os.system('cls')
        print(f"The answer is {res}")
        time.sleep(2)
        os.system('cls')

    elif c == "-1":
        os.system('cls')
        print("Thank you for using the calculator!")
        time.sleep(2)
        break

    print("Multiplication")

    n = float(input("Enter the number: "))

    t = 0  # Total number enter

    ans = 1

    while n != 0:

        ans = ans * n

        t += 1

        n = float(input("Enter another number (0 to calculate): "))

        return [ans, t]


def average(an):

    an = []

    an = addition()

    t = an[1]

    a = an[0]

    ans = a / t

    return [ans, t]

    # main...


while True:

    list = []

    print(" My first python program!")

    print(" Simple Calculator in python by FABEL404")

    print(" Enter 'a' for addition")

    print(" Enter 's' for subtraction")

    print(" Enter 'm' for multiplication")

    print(" Enter 'v' for average")

    print(" Enter 'q' for quit")

    c = input(" ")

    if c != "q":

        if c == "a":

            list = addition()

            print("Ans = ", list[0], " total inputs ", list[1])

        elif c == "s":

            list = subtraction()

            print("Ans = ", list[0], " total inputs ", list[1])

        elif c == "m":

            list = multiplication()

            print("Ans = ", list[0], " total inputs ", list[1])

        elif c == "v":

            list = average()

            print("Ans = ", list[0], " total inputs ", list[1])

        else:

            print("Sorry, invalid character")
    else:
        break
        os.system('cls')
        print("Sorry, invalid option!")
        time.sleep(2)
        os.system('cls')
