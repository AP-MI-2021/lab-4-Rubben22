def CitireLista():
    list = []
    citireLista = input("Dati lista: ")
    citireLista = citireLista.split(",")
    for x in citireLista:
        list.append(int(x))
    return list

def verificare_nr_prim(numar):
    """
    Verificam daca un numar este prim
    :param numar: Numarul pentru care se verifica
    :return: True daca este prim si false in caz contrar
    """
    if numar <= 1:
        return False
    elif numar == 2:
        return True
    elif numar > 2:
        for d in range(2, numar//2 + 1):
            if numar % d == 0:
                return False
    return True

def eliminare_nr_prim(nouaLista):
    """
    Functia elimina numerele prime din lista
    :param list: lista de numere
    :return: Noua lista de numere formata dupa eliminarea numerelor prime
    """
    for x in nouaLista:
        if verificare_nr_prim(x):
            nouaLista.remove(x)
    return nouaLista

def testeliminare_nr_prim():
    assert eliminare_nr_prim([2, 8, 16, 61]) == [8, 16]
    assert eliminare_nr_prim([15, 21, 13]) == [15, 21]

def media_aritmetica(list, n):
    """
    Verifica daca media aritmetica este mai mare decat un numar n dat
    :param list: lista de numere
    :param n: numarul dat
    :return: True daca este mai mare si False in caz contrar
    """
    suma = 0
    nrDeTermeni = 0
    for x in list:
        suma += x
        nrDeTermeni += 1
    media = suma// nrDeTermeni
    if media > n:
        return True
    else:
        return False

def test_media_aritmetica():
    assert media_aritmetica([4, 8, 3], 4) is True
    assert media_aritmetica([8,20], 50) is False

def nr_divizori_proprii(numar):
    """
    Calculeaza nr de divizori proprii ai unui numar
    :param numar: numarul dat
    :return: numarul de divizori
    """
    nrDivizori = 0
    for i in range(2, numar//2 + 1):
        if numar % i == 0:
            nrDivizori += 1
    return nrDivizori

def inserare_nr_divizori_in_lista(list):
    for i in list:
        numar = nr_divizori_proprii(i)
        list.append(int(numar))
    return list


def main():
    testeliminare_nr_prim()
    test_media_aritmetica()
    list = []
    nouaLista = []
    while True:
        print("1.Citire lista")
        print("2.Elimina elementele prime din lista")
        print("3.Afiseaza daca media aritmetica a numerelor este mai mare decat un n dat")
        print("4.Afiseaza lista obtinuta dupa adaugarea fiecarui numar de divizori proprii")
        print("a. Afisare lista")
        print("x. Iesire")
        optiune = (input("Alegeti o optiune: "))
        if optiune == "1":
            list = CitireLista()
        elif optiune == "2":
            nouaLista = list
            print(eliminare_nr_prim(nouaLista))
        elif optiune == "3":
            n = int(input("dati numarul n: "))
            if media_aritmetica(list, n):
                print("Este mai mare ")
            else:
                print("NU este mai mare")
        elif optiune == "4":
            print(inserare_nr_divizori_in_lista(list))
        elif optiune == "a":
            print(list)
        elif optiune == "x":
            break



if __name__ == "__main__":
    main()