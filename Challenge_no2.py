#def function for invalid inputs
def invalid(number):
    while True:
        try:
            return float(input(number))
        except ValueError:
            print("Invalid input, try again")

def invalid_2(number):
    while True:
        try:
            return int(input(number))
        except ValueError:
            print("Invalid input, try again")

#Smaller num
#"NOT EQUAL" when nums are not the same
#Difference of two numbers
#Quotient without decimal point
#remainder when 1st / 2nd        
num1 = invalid("num1: ")
num2 = invalid("num2: ")
if num1 != num2:
    print("Not Equal")
    if num1 > num2:
        print(f'{num2} is smaller')
    
    elif num1 < num2:
        print(f'{num1} is smaller')
        
print(f"Difference: {abs(num1-num2)}")
print(f"Quotient: {num1/num2:.0f}")
print(f"Remainder: {num1%num2}\n")

#1st num minus all the remaining number (10 inputs)
#in 10 input print all the even numbers
total = 0
even_cntr = 0
first_num = invalid("Input num1: ")
if first_num % 2 == 0:
        even_cntr += 1

for minus_total in range(2, 11):
    ask =  invalid(f"Input num{minus_total}: ")
    if ask % 2 == 0:
        even_cntr += 1
    else:
        continue
    total += ask
    
print(f"{first_num} - {total} = {first_num - total}")
print(f"total of even numbers:{even_cntr}\n")

#print all even numbers from 0 to 100 (use while loop)
#print all numbers that does not end with 5 or 0
cnt = 0
while cnt < 100:
    cnt += 1
    if cnt % 2 != 0:
        pass 
        if cnt % 5 != 0:
            print(cnt)
    else:
        continue

#print all numbers between the two numbers 
num1 = invalid_2("\nnum1: ")
num2 = invalid_2("num2: ")

for prnt in range(num1 + 1, num2):
    print(prnt)
