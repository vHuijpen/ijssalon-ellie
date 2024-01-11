print()
print ("__________________")
print()

def mijn_functie_2(a=12,b=3,c=12,d=2,e=10,f=5,g=100,h=20):
  taak1 = [a+3,a-3,b*12,b+1] 
  taak2 = [c+2,c-2,d*12,d*3]
  taak3 = [e+5,e-5,f*10,f-3]
  taak4 = [g+20,g-20,h*100,h-15]
  
  return taak1,taak2,taak3,taak4
print(mijn_functie_2())

(mijn_functie_2())



print()
print ("__________________")
print()




print()
def aanbieding_1(smaak,prijs,korting):
    print("Vandaag in de aanbieding, emmertje ijs (1 liter), in de smaak" , smaak , "van" , prijs , "euro, voor" , korting , "euro")

aanbieding_1 ("aardbei","4","3,60")




print()
print ("__________________")
print()


def inkomsten_totaal(inkomsten):
    a = [220,430,125,160,205,90,354]
    btw = sum(a) / 100 * 21
    print ("Het totaal van alle inkomsten van deze week is", sum(a), "euro, waarover", btw, "euro BTW betaald dient te worden." )

inkomsten_totaal(list)



print()
print ("__________________")
print()



def laag_en_hoog(mijn_lijst):
    mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
    hoog = max(mijn_lijst)
    laag = min(mijn_lijst)
    print(hoog)
    print(laag)

laag_en_hoog(list)


print()
print ("__________________")
print()


def gemiddelde(mijn_lijst):
    mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
    gemiddelde = sum(mijn_lijst) / 7
    print("De gemiddelde inkomsten van deze week zijn:", gemiddelde, "euro.")

gemiddelde(list)



print()
print ("__________________")
print()



def meervoudig(invoer_lijst):
    invoer_lijst = [10,5,3,2,1,2,9]
    n = min(invoer_lijst)
    x = max(invoer_lijst)
    print (n,x)

meervoudig(laag_en_hoog)



print()
print ("__________________")
print()



def combinatie(invoer_lijst_2):
    korte_lijst = meervoudig(invoer_lijst_2)
    return mijn_functie_2(korte_lijst)
