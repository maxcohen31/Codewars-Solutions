def insiemistica(lista1, lista2):
    insieme_vuoto = set{}

    print("Le operazioni risultano: ")

    if len(lista1) == 0 and len(lista2) == 0:
        print(f"Intersezione: {insieme_vuoto}")
        print(f"Unione: {insieme_vuoto}")
        print(f"Differenza: {insieme_vuoto}")

    elif len(lista1) > 0 and len(lista2) == 0:
        print(f"Intersezione: {insieme_vuoto}")
        print(f"Unione: {lista1}")
        print(f"Differenza: {lista1}")

    elif len(lista1) == 0 and len(lista2) > 0:
        print(f"Intersezione: {insieme_vuoto}")
        print(f"Unione: {lista2}")
        print(f"Differenza: {lista2}")

    elif len(lista1) > 0 and len(lista2) > 0:
        print(f'Unione:{lista1 | lista2}')
        print(f'Intersezione: {lista1 & lista2}')
        print(f'Differenza: {lista1 - lista2}')
        print(f'Differenza Simmetrica: {lista1 ^ lista2}')


