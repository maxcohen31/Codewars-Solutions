def dfs_cycle(G, v, u, P):
    P[v] = -u  # Il valore negativo indica che la visita è iniziata ma non è terminata
    for w in G[v]:
        if P[w] == 0:
            z = dfs_cycle(G, w, v, P)
            if z != 0:  # Un ciclo è già stato trovato
                P[v] = -P[v]
                return z
        elif P[w] < 0 and (is_directed or w != u):  # Trovato ciclo
            P[w] = 0  # Marca il primo nodo del ciclo
            P[v] = u
            return v
    P[v] = u  # La visita da u è terminata
    return 0  # senza aver trovato un ciclo

def find_cycle(G, is_directed=False):
    n = len(G)
    P = [0] * n  # Vettore dei padri inizializzato a 0
    
    for u in range(n):
        if P[u] == 0:
            w = dfs_cycle(G, u, u, P)
            if w > 0:
                L = []
                while w > 0:
                    L.append(w)
                    w = P[w]
                return L
    return None  # Nessun ciclo trovato

# Esempio di utilizzo:
# G rappresenta un grafo come lista di adiacenza.
# G = [[1, 2], [2], [0, 3], [3]] rappresenta un grafo diretto con un ciclo.
# is_directed = True se il grafo è diretto, False se è non diretto.
G = [[1, 2], [2], [0, 3], [3]]
is_directed = True
print(find_cycle(G, is_directed))
