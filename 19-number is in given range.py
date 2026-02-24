num = int(input("Enter number: "))
low = int(input("Enter lower range: "))
high = int(input("Enter upper range: "))

if low <= num <= high:
    print("Number is within range")
else:
    print("Number is outside range")