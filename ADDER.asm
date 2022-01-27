// inputs
X = 14  // 00001110
Y = 35  // 00100011


// program
SUM = X


Addstart:
    XOR SUM Y
    AND Y X
    JPZ addend

    X = SUM
    AND 0 0
    JPZ addstart


Addend:
    X = SUM  // 00110001
