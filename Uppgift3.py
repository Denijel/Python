# Programmeringsteknik webbkurs KTH inlämningsuppgift 3.
# <Denijel Becevic, 910603-7535>
# <2015-07-19>
# <Programmet är en simulering utav ett nöjesfält med 3 attraktioner>

from random import *

#Klassen nöjsfält som består av thre attraktions-objekt
class Nojesfalt(object):
    def __init__(self,min_langd,min_alder,namn_attraktion,beskrivning, akljud, haveri_varde):
        self.min_langd = min_langd
        self.min_alder = min_alder
        self.namn_attraktion = namn_attraktion
        self.beskrivning = beskrivning
        self.akljud = akljud
        self.haveri_varde = haveri_varde

#Funktion för att kolla längd och ålder på personen som skall åka
    def kolla_varden(self):
        pers_langd = int(input("hur lång är du?: "))
        pers_alder = int(input("Hur gammal är du?: "))
        if pers_langd < self.min_langd:
            print("du är tyvärr för kort...")
        elif pers_alder < self.min_alder:
            print("du är tyvärr inte gammal nog")
        else:
            print(self.akljud)

#Funktion som slumpar fram ett haveri.
#Om värdet på haveri:et överstiger attraktioners värde så havererar attraktionen
#Efter att haveri har testats, kolla programmet långd och ålder på personen
    def haveri(self):
        haverera = randrange(1,11)
        if haverera <= self.haveri_varde:
            print("Tyvärr är attraktionen ur funktion...")
        else:
            self.kolla_varden()

# HUVUDPROGRAM - detta skapar attraktionsobjekten och kör simuleringen
def huvudprogram():
    #skapa objekten
    attraktioner = [Nojesfalt(110,12,"Bergbanan","Den fartfyllda turen!","Swooosh!",3),Nojesfalt(100,14,"Spöktunneln","Ett vågat val!","Iiiih",2),Nojesfalt(90,8,"Slänggungan","För hela familjen!","Woohoo!",4)]

    #Val utan attraktion
    val = int(input("Hej! Välj en attraktion: \n" + "1.Bergbanan\n" + "2.Spöktunneln\n"+ "3.Slänggungan \n" + "4.Åka hem\n"))
    if val in range(1,4):
        #medan man väljer attraktion så ska programmet köras
        #Efter vald attraktion kan man se reklam, åka eller avsluta(gå tillbaka)
        while val in range(1,4):
            print(attraktioner[val-1].namn_attraktion +" - Vad vill du göra härnäst?")
            val2 = int(input("1.Se info\n" + "2.Åk\n" + "3.Gå tillbaka\n"))
            while  val2 == 1:
                print(attraktioner[val-1].beskrivning + "\n")
                break
            if val2 == 2:
                #kallar på haverifunktionen som först testar haveri och sen läng och ålder.
                attraktioner[val-1].haveri()
            elif val2 == 3:
                val = int(input("Hej! Välj en attraktion: \n" + "1.Bergbanan\n" + "2.Spöktunneln\n"+ "3.Slänggungan \n" + "4.Åka hem\n"))
                if val == 4:
                    print("Hoppas att du hade en bra dag! Välkommer åter!")
                    break
    #Om man vill åka hem så ska detta skrivas ut och programmet stängas
    else:
        print("Hoppas att du hade en bra dag! Välkommer åter!")





huvudprogram()