nam = input("Enter your First Name:\t")
mi = input("Enter your Middle Initial:\t")
surname = input("Enter your Surname:\t")
print(f"Full Name:\n{surname.capitalize()} {nam} {mi.upper()}")
y = 0
for x in range(1,11):
    ini = eval(input(f"{x} - Enter 10 Numbers:\t"))
    if ini % 2 == 1:
        y += ini
print(f"The Total Sum of the odd numbers are: {y}")