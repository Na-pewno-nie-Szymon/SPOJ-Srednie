from math import sqrt

def trojkatE(y1, x1, y2, x2, y3, x3, yD, xD):
    X = [x1, x2, x3]
    Y = [y1, y2, y3]
    
    if yD == ((y1 - y2)/(x1 - x2))*xD + (y1 - ((y1 - y2)/(x1 - x2))*x1):
        return True
    elif yD == ((y1 - y3)/(x1 - x3))*xD + (y1 - ((y1 - y3)/(x1 - x3))*x1):
        return True
    elif yD == ((y3 - y2)/(x3 - x2))*xD + (y1 - ((y3 - y2)/(x3 - x2))*x3):
        return True
    return False


def trojkatO(y1, x1, y2, x2, y3, x3, yD, xD):
    dl12 = sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2)
    dl13 = sqrt(abs(x1 - x3)**2 + abs(y1 - y3)**2)
    dl23 = sqrt(abs(x2 - x3)**2 + abs(y2 - y3)**2)

    X = [x1, x2, x3]
    Y = [y1, y2, y3]
    DL = [dl12, dl13, dl23]
    
    for i in range(3):
        c = 0
        for d in range(3):
            if sqrt(abs(X[i] - xD)**2 + abs(Y[i] - yD)**2) > DL[d] and c == 0:
                c += 1
            elif sqrt(abs(X[i] - xD)**2 + abs(Y[i] - yD)**2) > DL[d] and c > 0:
                return False
    return True

def trojkatI(y1, x1, y2, x2, y3, x3, yD, xD):
    dl12 = sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2)
    dl13 = sqrt(abs(x1 - x3)**2 + abs(y1 - y3)**2)
    dl23 = sqrt(abs(x2 - x3)**2 + abs(y2 - y3)**2)

    X = [x1, x2, x3]
    Y = [y1, y2, y3]
    DL = [dl12, dl13, dl23]
    for i in range(3):
        for d in range(3):
            if sqrt(abs(X[i] - xD)**2 + abs(Y[i] - yD)**2) > DL[d]:
                return False
    return True

def main():
    while True:
        x1, y1, x2, y2, x3, y3, x, y = map(int, input().split())
        if x1 == 0 and x2 == 0 and x3 == 0 and y1 == 0 and y2 == 0 and y3 == 0 and x == 0 and y == 0:
            break


        if trojkatE(x1 = x1, y1 = y1, x2 = x2, y2 = y2, x3 = x3, y3 = y3, yD = y, xD = x):
            print('E')
        elif trojkatI(x1 = x1, y1 = y1, x2 = x2, y2 = y2, x3 = x3, y3 = y3, yD = y, xD = x):
            print('O')
        else:
            print('I')
        
    return

if __name__=='__main__':
    main()
