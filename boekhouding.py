import pandas

from helper import*
from presentatie import*

inkomsten = {
    "Aardbeien-ijs-totaal" : 1000,
"Vanille-ijs-totaal" : 2000,
"Chocolade-ijs-totaal" : 1500,
"Water-ijsjes-totaal" : 750}

totaal_inkomsten = sum(inkomsten.values())

presenteer(inkomsten)