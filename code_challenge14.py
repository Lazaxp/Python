y = 0
x = ""
name = input("Hello, What is your name?\t")
print("++++++++++++++++++++++++++++++++++\nODD Number Compiler")
while True:
    num = eval(input("input an ODD number"))
    x = str(num)+","
    if num % 2 == 1:
        y += num
        print("odd number")
    elif num % 2 == 0:
        print("Even number,skipping")
    else:
        print("Invalid Number")
    if num == 0:
        print("process stopped")
        break
print(f"Hi {name}, the total ODD numbers summation is: {y}")
print("all odd numbers detected were",x)
