#defined functions
def greet(name):
    print(f"hi, {name} how you doing?")

def sum(a):
    x = 0 
    for y in range(a, 0,-1):
        x += y
    print(f"the sum of {a} is {x}")

greet("Luis")
sum(5)