tab = [[0,1,0,0,0,0],
       [0,0,1,0,1,0],
       [0,1,0,1,0,0],
       [0,0,1,0,1,1],
       [0,1,0,1,0,1],
       [0,0,0,1,1,0]]

##zwykła macierz przyległości wierzchołków grafu, ilość zadaych wierzchołków dowolna 


def kolorowanie(tab):
    m = len(tab)
    kolor = [0 for i in range(m)]
    for i in range(m):
        current = [0,0,[]] #dane (nr,stopien, kolory wierzcholkow prszyległych) aktualnie sprwadzanego wierzchołka 
        maks = [0,0,[]] # szuakny wierzchołek w danej iteracji
        z = 1
        j = 0
        while j < m:
            if (len(tab[j]) < m) and (j < m-1) :
                j+= 1 #pominiecie sprawdzania już pokolorowanych wierzchołków
            elif (len(tab[j]) < m) and (j == m-1):
                break    
            if len(tab[j]) == m:
                current[0] = j
                for k in range(m): #sprawdzanie konkretnego wierzchołka
                    if (tab[j][k] != 0):
                        current[1] += tab[j][k]
                        if (kolor[k] != 0) and (kolor[k] not in current[2]):
                            current[2].append(kolor[k])
                if len(maks[2]) <= len(current[2]):
                        if maks[1] < current[1]:
                            maks = current
                current = [0,0,[]]
            j += 1
        while(z in maks[2]):
            z += 1 #zachłanne kolorowanie wierzchołka
        kolor[maks[0]] = z
        tab[maks[0]] = [0]
    print(kolor)

        
kolorowanie(tab)

#funckaj zwraca tablice w której kazdy kolejny element to kolor kolejnego wierzchołka
#np, element pierwszy (kolor[0]) to kolor pierwszego wierzchołka, różne kolory są reprezentowane przez kolejne liczby naturalne
