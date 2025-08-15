deposit = eval(input("enter your deposit>>"))
print("type:",type(deposit))
t = deposit//1000
f = deposit//500-t*2
tw = deposit//200-(t*5)-(f*2)
on = deposit//100-(t*10)-(f*5)-(tw*2)
fi = deposit//50-(t*20)-(f*10)-(tw*5)-(on*2)
twe = deposit//20-(t*50)-(f*20)-(tw*10)-(on*5)-(fi*2)
ten = deposit//10-(t*100)-(f*50)-(tw*20)-(on*10)-(fi*5)-(twe*2)
fiv = deposit//5-(t*200)-(f*100)-(tw*50)-(on*20)-(twe*10)-(ten*5)
one = deposit//-(t*500)-(f*200)-(tw*100)-(on*50)-(twe*20)-(ten*10)-(fiv*5)
print("1000 =",t,"500 =",f,"200 =",tw,"100 =",on,"50 =",fi,"20 =",twe,"10 =",ten,"5 =",fiv,"1 =",one)
