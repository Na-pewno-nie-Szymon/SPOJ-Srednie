# 2 - abc
# 3 - def
# 4 - ghi
# 5 - jkl
# 6 - mno
# 7 - pqrs
# 8 - tuv
# 9 - wxyz

litery = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}

def wordCheck(slowa, liczby): # ja jebe, to jest takie obrzydliwe. Weź ty debilu pomyśl trochę bo jak tak dalej pójdzie to możesz jebać te zawody
    if len(slowa) != len(liczby):
        return 0
    else:
        for i in range(len(liczby)):
            if slowa[i] not in litery[str(liczby[i])]:
                return 0
    return 1

def main():  
    slowa = []
    liczby = []
    n, k = input().split()  # <= 100000   liczba wyrazów w slowniku
                            # <= 1000000  liczba liczb dla których szukamy wyrazów
    slowa = [input() for i in range(int(n))]    # uzupełnienie slow
    liczby = [input() for i in range(int(k))]   # uzupelnienie liczb

    for l in liczby:
        lista = []
        for s in range(len(slowa)-1):
            #print(f'TEST: slowo: {slowa[s]}\tLiczba: {l}\tBool: {wordCheck(slowa=slowa[s], liczby=l)}')
            if wordCheck(slowa=slowa[s], liczby=l):
                lista.append(slowa[s])
        for i in range(len(lista)):
            slowa.remove(lista[i])
        lista.sort()
        if len(lista)==0:
            print('BRAK')
        else: print(*lista)        
    
    return

if __name__=='__main__':
    main()  
