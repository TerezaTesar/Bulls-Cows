'''
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Tereza Tesar Ruzicka
email: tereza.ruza@gmail.com
discord: Tea #1877
'''

'''import knihoven'''
import random 

    
def main():
    '''spusti hru'''
    cislo = vytvor_cislo()
    pokusy = int(input('Napis kolikrat chces hadat: '))
    hra_bezi(cislo, pokusy)
    pass
   

def prevod_na_list(cislo:int) -> list:
    '''vrati list jednotlivych cislic hadaneho cisla'''
    return [int(i) for i in str(cislo)]
      

def unikatni_cislo(cislo:int) -> bool:
    '''kontrola unikatnosti cisla
    
    vrati True pokud zadna cislice neni dvakrat  '''
    list_cislic = prevod_na_list(cislo)
    if len(list_cislic) == len(set(list_cislic)):
        return True
    else:
        return False
  
   
def vytvor_cislo() -> int:
    '''generovani hadaneho cisla

    vygeneruje cislo z intervalu 1000-9999
    to zajisti aby cislo nezacinalo nulou'''
    while True:
        cislo = random.randint(1000,9999)
        if unikatni_cislo(cislo):
            return cislo
  
  
def pocty_byku_krav(cislo:int,hadani:int) -> list:
    '''pocty byku a krav
 
    pro kazdou cislici z hledaneho cisla (cislo) probehne porovnavani
    s cislici z uzivatelem zadaneho cisla (hadani)
    pokud nalezne shodu cislice i mista pricte jednoho byka
    pokud nalezne shodu jen cisla pricte kravu'''
    list_cislic = prevod_na_list(cislo)
    list_hadani = prevod_na_list(hadani)
    byci_kravy = [0,0]
    for i,j in zip(list_cislic,list_hadani):
          
        if j in list_cislic:
          
            if j == i:
                byci_kravy[0] += 1
              
            else:
                byci_kravy[1] += 1
                  
    return byci_kravy
        
  
def hra_bezi(cislo:int,pokusy:int) :
    '''osetreni vstupu a prubehu hry
    
    pomoci try and except hlida vstup od uzivatele
    ujisti se jestli chce hrat, pripadne mu da novy pokus
    take kontroluje jestli je cislo od uzivatele ctyrmistne 
    a unikatni
    v pripade ze se hadani a cislo rovnaji 
    nebo dojdou pokusy ukonci hru'''
    while pokusy > 0:
        try:
            hadani = int(input('Hadej ctyrmistne cislo: '))
        except ValueError:
                chces_hrat = input('Nezadal jsi cislo. Jestli chces hrat napis "ano":')
                if chces_hrat != 'ano':
                    print('Ukoncuji hru!')
                    quit()
                else: 
                    continue
        if not unikatni_cislo(hadani):
            print('V hadanem cisle se zadne cislice neopakuji, hadej znovu: ')
            continue
        if hadani < 1000 or hadani > 9999:
            print('Hadej ctyrmistne cislo: ')
            continue
        if hadani == cislo:
            print(f"Uhodl js! Hadane cislo je: {cislo}")
            break
        pokusy -= 1
        vypis = vypis_byku_kav(cislo,hadani)
        print(vypis)
    else:
        print(f"Dosly pokusy, hledane cislo bylo: {cislo}")
    


def vypis_byku_kav(cislo:int,hadani:int) -> str:
    '''osetreni vypisu
    
    meni vystup podle poctu uhodnutych byku a krav'''
    byci_kravy = pocty_byku_krav(cislo,hadani)
    byci = ['byku', 'byka', 'byky', 'byky','byky']
    kravy = ['krav', 'kravu', 'kravy', 'kravy', 'kravy']
    byk = byci_kravy[0]
    krava = byci_kravy[1]
    return (f"{byci_kravy[0]} {byci[byk]} a {byci_kravy[1]} {kravy[krava]}")
    

main()