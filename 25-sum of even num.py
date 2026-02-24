n = int(input("Enter N: "))
i = 1
sum = 0

while i <= n:
    if i % 2 == 0:
        sum += i
    i += 1

print("Sum of even numbers =", sum)