# Programmeringsteknik webbkurs KTH inlämningsuppgift 1.
# <Denijel Becevic, 910603-7535>
# <2015-06-30>
# <Programmet itererar fram ett Kaprekar-värde utifrån vald input samt räknar iterationer>


#nummer som väljs samt variabler för kaprekar och antal varv
nummer=int(input("Välj ett fyrsiffrigt tal: "))
KAPREKAR=6174

count=0


while nummer != KAPREKAR:

    n =str(nummer) #lagrar nummervärdet i värde n

    #om nummervärdet är tresiffrigt, sätts en 0:a framför (111 => 0111)
    if (len(str(nummer)) < 4):
        y = int(nummer)
        nummer = ('%04d' % y) #sätter in 0:a framför
        n = str(nummer)

    #talet sorteras och lagras som int-värde
    largeNum = int("".join(sorted(n, reverse=True)))

    smallNum = int("".join(sorted(n)))

    #Det största talet minus det minsta, samt lagras som nytt värde i ditt valda nummer
    nummer = largeNum - smallNum
    print(largeNum, '- ', smallNum, '= ', nummer)

    #iterationer + 1 för varje varv.
    count += 1

#När kaprekar-talet är uppfyllt skriver programmet ut hur många iterationer som behövdes

print("det tog", count, "iterationer att nå", nummer)