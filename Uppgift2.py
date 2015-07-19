# Programmeringsteknik webbkurs KTH inlämningsuppgift 2.
# <Denijel Becevic, 910603-7535>
# <2015-07-09>
# <Programmet skapar en rondelet-dikt utav fyra meningar som fylls i>

def intro():
    '''introduktionstext'''
    print (
"""                DIKTAUTOMATEN

Skriv in fyra meningar och få ut en rondelet!
""")
    return


def din_dikt(sentence):
    '''funktion för att samla meningar och lägga in det i en lång sträng.
    Denna funktion körs tills att man har skrivit in fyra meningar'''
    n=0
    while n < 4 :
        sentence[n] = input('skriv mening nr '+ str(n+1) + ' : ')
        n+=1
    return sentence

def skriv_rubrik(sentence):
    '''Skriver ut en rubrik av de fyra första orden med versaler'''
    rubrik = sentence[0].split()
    print('\n')
    for item in rubrik[:4]:
        rubrik = print("".join(item.upper()), end=" ")
    return rubrik


def skriv_dikt(sentence):
    '''Skriver ut hela dikten,
     1- lagrar varje mening i en egen lista
     2- Skriver ut strukturen på dikten'''
    mening1 = sentence[0].split()
    mening2 = sentence[1].split()
    mening3 = sentence[2].split()
    mening4 = sentence[3].split()
    for item in mening1[:4]:
        print("".join(item), end=" ")
    print('')
    #om första meningen har mindre än eller fyra ord ska en tom rad inte skrivas
    if len(mening1) > 4:
        for item in mening1[4:]:
            print("".join(item), end=" ")
        print('')
    for item in mening1[:4]:
        print("".join(item), end=" ")
    print('')
    # Om någon mening är tom skall inte en tom rad skrivas ut
    if len(mening2) > 0:
        print(" ".join(mening2))
    if len(mening3) >0:
        print(" ".join(mening3))
    if len(mening4) >0:
        print(" ".join(mening4))
    for item in mening1[:4]:
        print("".join(item), end=" ")
    print('')
    return mening1, mening2, mening3, mening4

## HUVUDPROGRAMMET SOM KÖR ALLT ##
def huvudprogram():
    sentence = 4*[None]
    intro()
    din_dikt(sentence)
    skriv_rubrik(sentence)
    print('\n')
    skriv_dikt(sentence)


huvudprogram()