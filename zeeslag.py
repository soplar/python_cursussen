import string
import random
import copy

def maak_bord():
    '''
Creert matrix van bepaalde rijen en kolommen
eerst 3 rijen en 4 kolommen
'''
    bord = {}
    for letter in letters[:rij]:
        for cijfer in cijfers[:kolom]:
            bord[f'{letter}{cijfer}'] = {'boot_aanwezig': False,
             'is_beschoten': False, 'raak' : False}
    return bord
                                         

def toon_bord(bord, einde=False):
    '''
Het bord wordt (voor nu) via een command window getoond
'''
    if einde:
        waarde = 'boot_aanwezig'
    else:
        waarde = 'is_beschoten'
        
    letters = sorted(set([x[0] for x in bord]))
    cijfers = sorted(set([int(x[1]) for x in bord]))
    print(' ',' '.join(letters))
    for cijfer in cijfers:
        print(cijfer, end=' ')
        for letter in letters:
            if bord[f'{letter}{cijfer}'][waarde] == False:
                print('X', end=' ')
            elif bord[f'{letter}{cijfer}']['raak']:
                print('*', end=' ')
            else:
                print('O', end=' ')
        print()
        
def plaatsen_schepen():
    '''
Plaatsen van 3 schepen, schepen raken elkaar noch
horizontaal noch verticaal!!!, ze worden random
geplaatst
'''
    for x in range(3):
        schip_plek = random.choice(mogelijke_plekken)
        bord[schip_plek]['boot_aanwezig'] = True
        
        verwijder_onmogelijke_plaatsen_schip(schip_plek)
        

def verwijder_onmogelijke_plaatsen_schip(plaatsing):
    '''
Bepaalt waar de boten WEL geplaatst mogen worden.
'''
    mogelijke_boven = f'{plaatsing[0]}{int(plaatsing[1]) - 1}'
    mogelijke_onder = f'{plaatsing[0]}{int(plaatsing[1]) + 1}'
    mogelijke_rechts = f'{letters[letters.index(plaatsing[0]) - 1]}{plaatsing[1]}'
    mogelijke_links = f'{letters[letters.index(plaatsing[0]) + 1]}{plaatsing[1]}'
    plekken = [mogelijke_boven, mogelijke_onder, mogelijke_rechts, mogelijke_links, plaatsing]
    for plek in plekken:
        if plek in mogelijke_plekken:
            mogelijke_plekken.pop(mogelijke_plekken.index(plek))
        

def schieten():
    '''
Speler schiet op een cel in de matrix (door bijvoorbeeld
D3 op te geven) bij mis print('Mis!') en geef bij de cel
aan dat er al eens geschoten is op de cel.
Bij raak print('Raak!) en geef bij de cel aan dat het raak was
'''
    beurten = 0
    sleutels = list(bord.keys())
    toon_bord(bord)
    while any(bord[sleutel]['boot_aanwezig'] for sleutel in sleutels):
        
        schot = input('Op welke cel wil je schieten?').upper()
        if bord[schot]['boot_aanwezig'] == True:
            print('Raak')
            bord[schot]['raak'] = True
            bord[schot]['boot_aanwezig'] = False
        else:
            print('Mis')
        bord[schot]['is_beschoten'] = True
        beurten += 1
        toon_bord(bord)
        
    print()
    toon_bord(bord_computer, einde=True) # nu met de pc gekozen plekken

    print(f'Gefeliciteerd je had maar {beurten} beurten nodig.')

    
if __name__ == '__main__':
    letters = string.ascii_uppercase
    cijfers = list(range(1,100))

    rij = 4
    kolom = 3
    bord = maak_bord()
    mogelijke_plekken = list(bord.keys())
    plaatsen_schepen()
    bord_computer = copy.deepcopy(bord)
    schieten()



