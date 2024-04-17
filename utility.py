def stampaDizionario(diz):
    for key,value in diz.items():
        print("la chiave è...."+key)
        print("il valore è...."+str(value))   

dizionario={"rossi":18,"bianchi":16,"verdi":6}
#inserire un elemento dentro al dizionario
dizionario["viola"]=14
print(dizionario)
#modificare una copia chiave valore
dizionario["bianchi"]=18
print(dizionario)

stampaDizionario(dizionario)
#iterare sul dizionario

    #calcolare il totale delle ore del dizionario
def sommaore(diz):
    somma=0
    for key,value in dizionario.items():
        somma=somma+value
        print(somma)

    #numero degli insegnati con cattedra piena
i=0
def orepiene(diz):
    for key,value in dizionario.items():
        if value==18:
            i=i+1

print("il numero degli insegnati con le ore piene è..."+str(i))       

def cambiaore(diz,professore,ore):
    if professore in diz:
        diz[professore]=ore
        
cambiaore(dizionario,"bianchi",6)       
print(dizionario)