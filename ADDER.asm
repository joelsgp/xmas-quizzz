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
    // bit 2^0
    A = Y
    XOR A 254
    JPZ shiftzero
    XOR CARRY 2
    Shiftzero:
    // bit 2^1
    A = Y
    XOR A 253
    JPZ shiftone
    XOR CARRY 4
    Shiftone:
    // bit 2^2
    A = Y
    XOR A 251
    JPZ shifttwo
    XOR CARRY 4
    Shifttwo:
    // bit 2^3
    A = Y
    XOR A 247
    JPZ shiftthree
    XOR CARRY 8
    Shiftthree:
    // bit 2^4
    A = Y
    XOR A 239
    JPZ shiftfour
    XOR CARRY 16
    Shiftfour:
    // bit 2^5
    A = Y
    XOR A 223
    JPZ shiftfive
    XOR CARRY 32
    Shiftfive:
    // bit 2^6
    A = Y
    XOR A 191
    JPZ shiftsix
    XOR CARRY 64
    Shiftsix:

    // return if no carry
    AND CARRY 1
    JPZ addend

    // loop if carry
    X = SUM
    AND 0 0
    JPZ addstart

Addend:
    X = SUM  // 00110001
