#Hands-on 1 ITCS103
import os
numlist = []

print("Welcome, this Hands-On 1\n")
word = input("Type any word:\t").capitalize()
os.system("cls")
print(f"Word Input: {word}\nWord Length: {len(word)}\n(Please Use Double Digit numbers only)\n")
def ave(word):
    total = 0
    for x in range(len(word)):    
        numbers = eval(input("Enter a Number:\t"))
        numlist.append(numbers)
        total += numbers
    average = total / len(word)
    return average,total
average, total = ave(word)
def compare(average):
    if average <= len(word):
        return (f"Your word ({word}) word length is LESS than the AVERAGE of your number inputs: {average}")
    elif average >= len(word):
        return (f"Your word ({word}) word length is GREATER than the AVERAGE of your number inputs: {average}")
    else:
        return (f"Your word ({word}) word length is EQUAL than the AVERAGE of your number inputs: {average}")
os.system("cls")
print(f"Word Input: {word}\nWord Length: {len(word)}\nNumber Inputs: {numlist}\nTotal: {total}\nAverage: {average}\n")
print(compare(average))



