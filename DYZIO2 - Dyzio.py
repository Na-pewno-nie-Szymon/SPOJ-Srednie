from math import sqrt, ceil # z jakiegoś powodu spoj wypluwa mi błędną ospowiedź na zmianę z przekroczeniem limitu czasu :ccc

# sito erastotenesa
# tworzymy listę z przedziało podanego w zadaniu, czyt x <= 106
# True - oznacza liczbę pierwszą; False - liczbę niepierwszą
liczby = [True for i in range(107)]
for i in range(2, int(ceil(sqrt(106)))):
    if liczby[i]:
        for k in range(i*i, 107, i):
            liczby[k] = False
liczby[0], liczby[1] = False, False

# Liczymy ilość liczb pierwszych z podanych metodzie granic zamkniętych
# I zwracamy tę ilość
def zadanie(start, end):
    c = 0
    for i in range(start, end + 1):
        if liczby[i]:
            c += 1
    return c

# Główne ciało zadania
def main():
    test = int(input()) # liczba testow
    
    wynik = []
    for t in range(test):
        a, b = map(int, input().split())    # granice
        wynik.append(zadanie(start=a, end=b)) # wynik zapisywany od razu do listy

    for result in wynik: # wypluwany wynik
        print(result)

if __name__=="__main__": 
    main()
    
    # === # Test sita erastotenesa # === #
    # for i in range(len(liczby)):       #
    #     print(f'{i}: {liczby[i]}')     #
    # === #                        # === #
