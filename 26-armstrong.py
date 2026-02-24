num = int(input("Enter number: "))
temp = num
sum = 0

while num > 0:
    digit = num % 10
    sum += digit ** 3
    num //= 10

if sum == temp:
    print("Armstrong Number")
else:
    print("Not Armstrong")