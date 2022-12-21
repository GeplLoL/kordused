from math import *
from random import *
from time import *
##5
#tuba = int(input("Mitu toa korteris: "))
#for i in range(1,tuba+1,1): #range(n) i=0,1,2,3,...,n-1
#    kraade = float(input(f"{i}. toa kraade: "))
#    if kraade>18:
#        print("Soe")
#    else:
#        print("Külm")

##6
#print("")
#people = randint(1,20)
#p=k=l=0
#print("Kokku on ",people, "inimest")
#for i in range(1,people+1,1):
#    pikkus= randint(140,200)
#    if pikkus>140 and pikkus<174:
#        print("lühike")
#        l+=1
#    elif pikkus>=175 and pikkus<=185:
#        print("keskmine")
#        k+=1
#    elif pikkus>=186 and pikkus<=200:
#        print("pikk")
#        p+=1
#print(f"Keskmine: {k}\nPikk: {p}\nLühike: {l}")
#people = randint(1,20)
#pikkus = randint(140,200)
#p=k=l=0
#print("Kokku on ",people, "inimest")
#while people>0:
#    people-=1
#    pikkus= randint(140,200)
#    if pikkus>140 and pikkus<174:
#        print("lühike")
#        l+=1
#    elif pikkus>=175 and pikkus<=185:
#        print("keskmine")
#        k+=1
#    elif pikkus>=186 and pikkus<=200:
#        print("pikk")
#        p+=1

#print(f"Keskmine: {k}\nPikk: {p}\nLühike: {l}")


##7
#print("")
#kasv = float(input("Kirjutage oma vanus: "))
#sugu = input("sisestage oma sugu(mees or naine): ")
#if sugu=="mees":
#    if kasv<=0 or kasv>250:
#        print("sa oled looduse viga")
#    elif kasv<=170:
#        print("see on madala tõusuga")
#    elif kasv>171 and kasv<185:
#        print("on keskmine kõrgus")
#    elif kasv>186:
#        print("see on pikk")
#    else:
#        print("sa oled looduse viga")
#elif sugu=="naine":
    
#    if kasv<=0 or kasv>250:
#            print("sa oled looduse viga")
#    elif kasv<=160:
#            print("see on madala tõusuga")
#    elif kasv>161 and kasv<175:
#            print("on keskmine kõrgus")
#    elif kasv>176:
#            print("see on pikk")
#else:
#    print("sa oled looduse viga")
#print("")
##8
#try:
#    piima = input("piima hind või mitte: ")
#    saia = input("saia hind või mitte: ")
#    leib = input("leiva hind või mitte: ")
#    if piima=="mitte" and saia=="mitte" and leib=="mitte":
#        piima=0
#        saia=0
#        leib=0
#        print("ei ole")
#    elif piima.isdigit() and saia.isdigit() and leib.isdigit():
#        print(int(piima)+int(saia)+int(leib))
#    elif piima=="mitte" and saia=="mitte":
#        iima=0
#        saia=0
#        print(int(piima+int(saia)))
#    elif piima=="mitte" and leib=="mitte":
#        piima=0
#        leib=0
#        print(int(piima)+int(leib))
#    elif piima=="mitte":
#        piima=0
#        print(int(piima)+int(saia)+int(leib))
#    elif saia=="mitte" and piima=="mitte":
#        saia=0
#        piima=0
#        print(int(saia)+int(piima)+int(leib))
#    elif saia=="mitte" and leib=="mitte":
#        saia=0
#        leib=0
#        print(int(saia)+int(leib)+int(piima))
#    elif saia=="mitte":
#        saia=0
#        print(int(saia)+int(leib)+int(piima))
#    elif leib=="mitte" and piima=="mitte":
#        leib=0
#        piima=0
#        print(int(leib)+int(piima)+int(saia))
#    elif leib=="mitte" and saia=="mitte":
#        leib=0
#        saia=0
#        print(int(leib)+int(saia)+int(piima))
#    elif leib=="mitte":
#        leib=0
#        print(int(leib)+int(saia)+int(piima))
#except:
#    print("error")
#print("")
##9
#a = input("väljaku pool a: ")
#a2 = input("väljaku pool b: ")
#while a.isdigit()>0 or a2.isdigit()>0:
#    if a==a2:
#        print("ruut")
#        print("")
#        break
#    else:
#        print("ei ruut")
#        a = input("väljaku pool a: ")
#        a2 = input("väljaku pool b: ")

a = input("väljaku pool a: ")
while a.isalpha():
    a = input("väljaku pool a: ")
    if a.isdigit()>0:
        a2 = input("väljaku pool b: ")
        if a2.isalpha():
            a2 = input("väljaku pool b: ")
        else:
            if a==a2:
                print("ruut")
            else:
                print("ei ruut")
                

    



         
            
       



#10
try:
    a = float(input("a: "))
    b = float(input("b: "))
    c = input("millist toimingut soovite teha: ")
    if c=="+":
        c=a+b
        print(c)
    elif c=="-":
        c=a-b
        print(c) 
    elif c=="*":
        c=a*b
        print(c)
    elif c=="/":
        c=a/b
        print(c)
    else:
        print("error")
except:
    print("andmete sisestamise viga")
print("")
#11
try:
    user = float(input("kui vana sa oled: "))
    if user/5==int(user/5):
        print("sul on aastapäev")
    else:
        print("ok")
except:
    print("andmete sisestamise viga")
print("")
#12
hind = float(input("toote hind: "))
if hind<10:
    vastus=hind-(hind*0.1)
    print(vastus)
elif hind>10:
    vastus=hind-(hind*0.2)
    print(vastus)
else:
    print("error")
print("")
#13
try:
    sugu = input("Mis on sinu sugu?(mees or naine) ")
    if sugu=="mees":
        age = int(input("kui vana sa oled? "))
        if age>=16 and age<=18:
            print("sa sobid meile")
        else:
            print("sa pole õiges vanuses")
    elif sugu=="naine":
        print("lubatud ainult mehed")
except:
    print("andmete sisestamise viga")
