#Övning 3, 2b
#2b Gör om programmet så att användaren kan skriva in en procentsats.
#Testa genom att hitta på en procentsats och räkna ut vad programmet ska svara med, innan du kör det. Till exempel 10%, som är 200 kr. Då ska jackan kosta 2000 - 200 == 1800 kr.
print ("\n""ÖVNING 3, 2b")
pris2 = 2000
RabattProcentStr = input("Vilken rabatt i procent är det på jackan? ")
RabattProcentInt = int(RabattProcentStr)
print ("Du angav rabatten: " +str(RabattProcentStr) +"%")
RabattKronor = pris2 * RabattProcentInt/100
slutPrisKronor = pris2 - RabattKronor
#print ("Priset för jacka nummer 2 efter rabatt är "+str(slutPrisKronor) +" kronor")
print (f"Priset för jacka nummer 2 efter rabatten {RabattProcentInt}% är {slutPrisKronor:.0f} kronor")