print()
def mijn_functie_1(a=2,b=4,c=10,d=12):
    taak = a*a,b*b,c*c,d*d
    return taak

print (mijn_functie_1())


print()
print("---------")

print()

def mijn_functie_2(a=12,b=3,c=12,d=2,e=10,f=5,g=100,h=20):
  taak1 = [a+3,a-3,b*12,b+1]
  taak2 = [c+2,c-2,d*12,d*3]
  taak3 = [e+5,e-5,f*10,f-3]
  taak4 = [g+20,g-20,h*100,h-15]
  
  return taak1,taak2,taak3,taak4
print(mijn_functie_2())

(mijn_functie_2())