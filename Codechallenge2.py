deposit = eval(input("enter your deposit>>"))
print("type:",type(deposit))
t = deposit//1000
f = deposit//500-t*2
tw = deposit//200-(t*5)-(f*2)
on = deposit//100-(t*10)-(f*5)-(tw*2)
fi = deposit//50-(t*20)-(f*10)-(tw*4)-(on*2)
twe = deposit//20-(t*50)-(f*25)-(tw*10)-(on*5)-(fi*2)
ten = deposit//10-(t*100)-(f*50)-(tw*20)-(on*10)-(fi*5)-(twe*2)
fiv = deposit//5-(t*200)-(f*100)-(tw*40)-(on*20)-(fi*10)-(twe*4)-(ten*2)
one = deposit//1-(t*1000)-(f*500)-(tw*200)-(on*100)-(fi*50)-(twe*20)-(ten*10)-(fiv*5)
print("1000 =",t,"\n500 =",f,"\n200 =",tw,"\n100 =",on,"\n50 =",fi,"\n20 =",twe,"\n10 =",ten,"\n5 =",fiv,"\n1 =",one)
