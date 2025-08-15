deposit = eval(input("enter your deposit>>"))
print("type:",type(deposit))
t = deposit//1000
f = (deposit % 1000)//500
tw = (deposit % 1000 % 500)//200
on = (deposit % 1000 % 500 % 200)//100
fi = (deposit % 1000 % 500 % 200 % 100)//50
twe = (deposit % 1000 % 500 % 200 % 100 % 50)//20
ten = (deposit % 1000 % 500 % 200 % 100 % 50 % 20)//10
fiv = (deposit % 1000 % 500 % 200 % 100 % 50 % 20 % 10)//5
one = (deposit % 1000 % 500 % 200 % 100 % 50 % 20 % 10 % 5)//1
print("1000 =",t,"\n500 =",f,"\n200 =",tw,"\n100 =",on,"\n50 =",fi,"\n20 =",twe,"\n10 =",ten,"\n5 =",fiv,"\n1 =",one)
