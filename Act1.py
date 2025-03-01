def invalid():
    while True:
        try:
            num = float(input("Enter a number: "))
            return num
        except ValueError:
            print("Invalid input, try again.")

def invalid_loop(num):
    while True:
        try: 
            num = float(input(f"Enter a number {num}: "))
            return num
        except ValueError:
            print("Invalid input, try again.")
        
#no1: Create a program that ask user to input 2 numbers. Print the bigger number.
num1 = invalid()
num2 = invalid()

if num1 < num2:
    print(f"{num2} is greater than {num1}\n")

#no2: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are equal
elif num1 == num2:
    print("Equal\n")

else:
    print(f"{num1} is greater than {num2}\n")

#no3: Create a program that ask user to input 2 numbers. Print the sum of the 2 nums
print(f"sum = {num1 + num2}\n")

#no4: Create a program that ask user to input 2 numbers. Print the product
print(f"product = {num1 * num2}\n")

#no5: Create a program that ask user to input 2 numbers. Print the quotient
print(f"quotient = {num1 / num2}\n")

#no6: Create a program that ask user to input 2 numbers. Print the results when num1 is raised to num2
print(f"power = {pow(num1, num2)}\n")

#no7: Create a program that ask user to input 10 numbers. Print the sum of all the numbers 
#no8: Create a program that ask user to input 10 numbers. Print how many are odd nums
total = 0
odd_total = 0
for ask in range(1, 11):
    num = invalid_loop(ask)
    total += num

    if num % 2 != 0:
        odd_total += 1

print(f"total: {total}\n")
print(f"total of odd numbers: {odd_total}\n")

#no9: Create a program that prints all the even nums starting from 0 to 100 (Use for-loop)
for count_even in range(0, 101):
    if count_even == 0:
        print(count_even)

    elif count_even % 2 == 0:
        print(count_even)
print("==End==\n")

#no10: Create a program that print all the nums starting from 0 to 100 except ending with zero(0).
for cnt in range(0, 101):
    cnrt_str = str(cnt) #convert string
    if cnrt_str.find("0") == True: #convert string
        continue
    elif cnt == 0:
        continue
    else:
        print(int(cnt))
print("==End==")
