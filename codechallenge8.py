#Display a multiplication table based upon user Input.
print("Multiplication Table Display\n")
numero = eval(input("Input a Number from 1-9:\t"))
for x in range (1,11):
    disp = numero * x
    print(numero,"x",x,"=",disp)