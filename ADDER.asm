// inputs
X = 14  // 00001110
Y = 35  // 00100011


// program
SUM = X

Addstart:
    // XOR for sum
    XOR SUM Y

    // AND, then left shift for carry
    AND Y X
    CARRY = 0
    // BIT 2^0
    A = Y
    XOR A 254
    JPZ zero
    XOR CARRY 2
    Zero:


    // return if no carry
    JPZ addend

    // loop if carry
    X = SUM
    AND 0 0
    JPZ addstart

Addend:
    X = SUM  // 00110001
