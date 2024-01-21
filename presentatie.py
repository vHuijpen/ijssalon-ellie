from helper import onderstreep

mijn_dict = {
    'vis' : 10,
  'vlees': 25,
    'overig' : 15}


def presenteer(d):
    
    totaal = 0
    for key, value in d.items():
        print (f"{key}:{value}")
        totaal += value
    print("=============================")
    print(f"\nTotaal:", {totaal})


presenteer(mijn_dict)