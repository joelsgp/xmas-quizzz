// inputs
X = 14  // 00001110
Y = 35  // 00100011


// program
SUM = X
CARRY = Y

Addstart:
    XOR SUM Y
    AND CARRY X
    XOR CARRY SUM
    JPZ addend

    X = SUM
    Y = CARRY
    AND 0 0
    JPZ addstart


Addend:
    X = SUM  // 00110001
