temp = eval(input("What is the Tempreture?\t")
if temp <= (-1):
  print("Temperature is; Freezing Cold")
elif temp >= 1 and temp <= 20:
  print("Temperature is; Cold")
elif temp >= 21 and temp <= 30:
  print("Temperature is; Lukewarm")
elif temp >= 31 and temp <= 40:
  print("Temperature is; Warm")
elif temp >= 41 and temp <= 50:
  print("Temperature is; Hot")
elif temp >= 51:
  print("Temperature is; Boiling Hot")
else:
  print("?")
