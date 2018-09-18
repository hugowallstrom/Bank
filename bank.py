print("*** Hej och välkommen till Pizzamakaren ***")#start medelande
print("1. Sätt in pengar. \n"
+ "2. Ta ut pengar. \n"
+ "3. Skriv ut ditt saldo. \n"
+ "4. Avsluta.")#Valen man har att välja på
saldo= 0
meny = 0#default värden
while meny != 4:#medans man inte har valt 4, så fortsätter programmet.
    try:
        meny = int(input("Gör ett val från menyn: "))#prompt för att göra ett val
    except:
        print("Du måste ange en siffra!")#om man skriver fel
    
    if meny == 1:
        try:
            saldo = saldo +int(input("Sätt in pengar: "))  #läger till på värdet
        except:
            print("Ange med siffor!")
    elif meny == 2:
        try:
            saldo = saldo -int(input("Ta ut pengar: "))#tar bort från värdet
        except:
            print("Med siffror!")
    elif meny == 3:
        print("Din saldo är: ", saldo)#skriver ut värdet
    elif meny ==4:
        print("Hej då!")#avslutar programmet
    else:
        print("Du gjorde inte ett korrekt val, prova igen.")#Fel medelande