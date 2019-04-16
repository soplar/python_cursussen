##vraag om de grootte van het intern geheugen (in GB)
geheugen = int(input("geef de grootte van het intern geheugen in GB: "))
##controleer of het intern geheugen groter of gelijk is aan 8
if geheugen >= 8:
##indien ja: exchange installeren
    print("je kunt exchange 2016 installeren")
##indien nee: exchange niet installeren
else:
    print("je kunt exchange 2016 niet installeren")
