a = int(input("Enter first: "))
b = int(input("Enter second: "))
c = int(input("Enter third: "))
d = int(input("Enter fourth: "))

largest = a

if b > largest:
    largest = b
if c > largest:
    largest = c
if d > largest:
    largest = d

print("Greatest number =", largest)