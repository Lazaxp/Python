#use for loops to ask user 10 numbers and add the sum
num = 0
for x in range (10):
    sum = eval(input("Input 10 numbers\t>>"))
    num += sum
    print("Current Total:",num)
print("The Total is",num)