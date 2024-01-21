import numpy as numpy

def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()


def fooi_pp(bedrag,personen):
    bedrag_pp = bedrag / personen
    return f"Het bedrag per persoon is: {bedrag_pp},- euro."


def onderstreep(tekst= "=" ):
    uit = []
    uit.append(tekst)
    uit.append(len(tekst)* "=")
    return uit


inkomsten = {
    "Aardbeien-ijs-totaal" : 1000,
"Vanille-ijs-totaal" : 2000,
"Chocolade-ijs-totaal" : 1500,
"Water-ijsjes-totaal" : 750}



def som():
    totaal = sum(inkomsten.values())
    print (f"Dit is de uitkomst:", [totaal])