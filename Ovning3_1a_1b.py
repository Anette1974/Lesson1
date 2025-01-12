#Övning 3, 1a
# Använd input för att be användaren om ett heltal. Spara värdet i en variabel. Omvandla variabelns värde till ett heltal, och skriv ut det för att testa om du har gjort rätt.
#Kodexempel med input:
#x = input("Fråga här")
print ("\n""ÖVNING 3, 1a")
heltal1Str = input("Skriv ett heltal: ")
heltal1Int = int(heltal1Str)
print ("Du skrev in heltalet: " +str(heltal1Int)) # Varför fungerar inte detta?? Svar, jag var tvungen att omvandla till sträng

#Övning 3, 1b
#Fråga användaren efter ett annat heltal. Skriv ut summan av talen, alltså tal1 + tal2.
#Testa genom att hitta på två tal och räkna ut summan i huvudet. Kontrollera om programmet räknar rätt.
print ("\n""ÖVNING 3, 1b")
heltal2Str = input("Skriv ett heltal till: ")
heltal2Int = int(heltal2Str)
print ("Ditt andra heltal var: " +str(heltal2Int))
summaInt = heltal1Int+heltal2Int
print ("Summan av dessa två heltal är: " +str(summaInt))