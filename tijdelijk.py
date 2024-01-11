from helper import decoreer
def print_aanbieding():
    prijzen = {
        "aardbei" : "3",
        "vanille" : "4",
        "chocolade" :"5"
        }
    aanbieding = 3 * 0.8
    reclame_tekst =(f"Vandaag in de aanbieding: aardbeien-ijs, 1 liter - slechts € {aanbieding}").format(aanbieding)
    reclame_tekst2 = reclame_tekst[:65]
    reclame_tekst3 = reclame_tekst2.upper()
    reclame_tekst4 = reclame_tekst3.split() 
    e1 = reclame_tekst4
    for i in e1:
        if len(i) >4:
            print(i.upper())
        else:
            print(i.lower())
    
decoreer("aanbieding")
print_aanbieding()