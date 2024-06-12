"""
    Algoritmo per determinare se un grafo è ciclico o meno.

    Se il grafo non è diretto (e connesso), 
    la presenza di un qualsiasi arco all'indietro indica l'esistenza di un ciclo. E se
    non ci sono archi all'indietro il grafo è aciclico perchè coincide con l'albero della DFS.
    Lo stesso vale per grafi diretti, cioè il grafo ha un ciclo se e solo se c'è almeno un arco all'indietro. 
    Per vederlo supponiamo che u0, u1,…,uk sia un ciclo (orientato e semplice) di G, 
    quindi u0 = uk. Supponiamo, senza perdita di
    generalità, che u0 sia il primo nodo del ciclo ad essere visitato dalla DFS. Siccome tutti gli altri nodi del ciclo
    saranno visitati durante la DFS da u0, l'arco (uk - 1, u0) è necessariamente un arco all'indietro. Dobbiamo ora far
    vedere che se c'è un arco all'indietro, c'è un ciclo. Sia (w, v) un arco all'indietro. Siccome v è un antenato di w,
    nell'albero della DFS c'è un cammino (orientato e semplice) che va da v a w e quindi l'arco (w, v) chiude tale
    cammino in un ciclo.
    Vediamo nel dettaglio come determinare se un grafo G ha dei cicli e in caso affermativo trovare uno di questi. Nel
    caso di grafi non diretti, nel cercare un arco all'indietro da un certo nodo v bisogna prestare attenzione a non
    confonderlo con l'arco che collega v al genitore (cioè l'arco che ha permesso di scoprire v). Per recuperare il ciclo
    dopo averlo trovato possiamo memorizzare, durante la DFS, l'albero di visita. Per rappresentare un albero radicato
    (o una arborescenza) risulta spesso utile una semplice struttura chiamata vettore dei padri che consiste in un array
    di n elementi P tale che P[v] contiene il padre del nodo v nell'albero e se u è la radice P[u] = u . Assumiamo
    che i nodi siano identificati dagli interi da 1 a n. 
    All'inizio della visita dal nodo v , per marcare che la visita è iniziata
    ma non ancora terminata, porremo P[v] <- -u , dove u è il padre di v . Quando la visita da v termina, porremo
    P[v] <- u . In questo modo, un arco che collega v a un suo adiacente w è un arco all'indietro se e solo se P[w]
    < 0 e w non è il padre di v (quest'ultima condizione è necessaria solamente per grafi non diretti)
"""

def dfs(graph, v, u, p):

    p[v] = -u # Valore negativo: visita iniziata ma non terminata

    for neighbor in graph[v]:
        if p[neighbor] == 0:
            visit = dfs(graph, neighbor, v, p)

            if visit != 0: # Un ciclo è già stato trovato
                p[v] = -p[v]
                return visit

        elif (p[neighbor] < 0) and (is_directed or neighbor != u): # Trovato ciclo
            p[neighbor] = 0 # Marca primo nodo a zero
            p[v] = u
            return v

    p[v] = u # Visita da u terminata
    return 0 # Nessun ciclo trovato

def find_cycle(graph, is_directed=False):
    
    # Vettore dei padri
    p = [0] * len(graph)

    for node in range(len(graph)):
        if p[node] == 0:
            visit = dfs(graph, node, node, p)

            if visit > 0:
                c = []
                while visit > 0:
                    c.append(visit)
                    visit = p[visit]
                return c
    # Nessun ciclo trovato
    return None

if __name__ == "__main__":
    g = [[1, 2], [2], [0, 3], [3]]
    is_directed = True
    print(find_cycle(g, is_directed))
