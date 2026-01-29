#Hands-on 1 ITCS103
import os
numlist = []
total = 0 
print("Welcome, this Hands-On 1\n")
word = input("Type any word:\t").capitalize()
os.system("cls")
print(f"Word Input: {word}\n(Please Use Double Digit numbers only)\n")
for x in range(len(word)):
    numbers = eval(input("Enter a Number:\t"))
    numlist.append(numbers)
    total+=numbers
average = total / len(word)
os.system("cls")
print(f"Word Input: {word}\nWord Length: {len(word)}\nNumber Inputs: {numlist}\n")
if average <= len(word):
    print(f"Your word ({word}) word length is LESS than the AVERAGE of your number inputs: {average}")
elif average >= len(word):
    print(f"Your word ({word}) word length is GREATER than the AVERAGE of your number inputs: {average}")
else:
    printf(f"Your word ({word}) word length is EQUAL than the AVERAGE of your number inputs: {average}")