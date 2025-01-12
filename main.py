# Veckouppgift 1
# Övning 1
#https://github.com/Anette1974/Lesson1.git
print ("ÖVNING 1")
first_name = "Anette"
last_name = "Cedergren"
print ("Hello world")
print ("This program was made by " +first_name +" "+last_name +"\n")

# Övning 2
'''
2 Diskutera i grupp
Rätta eventuella fel. Vad gör koden?
x = 100  # biljettpris
y = 200  # pengar på fickan
print("Det blir " + (y - x) " kronor över.")
z = 200 - 100 / 2
print("Hälften är: " + z)
Kom på bättre namn, i stället för x, y och z.
'''
print ("ÖVNING 2")
biljettpris = 100  # biljettpris
kontanter = 200  # pengar på fickan
print("Det blir " + str(kontanter - biljettpris) + " kronor över.")  # Konvertera resultatet till sträng
z = 200 - 100 / 2
print("Hälften är: " + str(z))  # Konvertera z till sträng

# Övning 3
'''
3 Använda variabler och datatyper
1a Använd input för att be användaren om ett heltal. Spara värdet i en variabel. Omvandla variabelns värde till ett heltal, och skriv ut det för att testa om du har gjort rätt.
Kodexempel med input:
x = input("Fråga här")

1b Fråga användaren efter ett annat heltal. Skriv ut summan av talen, alltså tal1 + tal2.
Testa genom att hitta på två tal och räkna ut summan i huvudet. Kontrollera om programmet räknar rätt.

2a Nu är det dags att köpa vinterkläder. Du ser en fin jacka som kostar 2000 kronor. Jackan är på rea, 50%. Skriv ett program som räknar ut hur mycket du behöver betala.
Tips: räkna ut rabatten med formeln: slut_pris = pris * rea_procent / 100.

2b Gör om programmet så att användaren kan skriva in en procentsats.
Testa genom att hitta på en procentsats och räkna ut vad programmet ska svara med, innan du kör det. Till exempel 10%, som är 200 kr. Då ska jackan kosta 2000 - 200 == 1800 kr.
'''
#Övning 3, 1a
print ("\n""ÖVNING 3, 1a")
heltal1Var = input("Skriv ett heltal: ")
heltal1Int = int(heltal1Var)
print ("Du skrev in heltalet: " +str(heltal1Int)) # Varför fungerar inte detta?? Svar, jag var tvungen att om vandla till sträng

#Övning 3, 1b
print ("\n""ÖVNING 3, 1b")
heltal2Var = input("Skriv ett heltal till: ")
heltal2Int = int(heltal2Var)
print ("Ditt andra heltal var: " +str(heltal2Int))
summaInt = heltal1Int+heltal2Int
print ("Summan av dessa två heltal är: " +str(summaInt))

#Övning 3, 2a
print ("\n""ÖVNING 3, 2a")
