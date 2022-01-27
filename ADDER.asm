// inputs
// X = 14  // 00001110
// Y = 35  // 00100011
// commented out for the sake of automated testing (test_adder.py)


// program

// x + y = (x ^ y) + ((x & y) << 1)
// left shift implemented with the horrible copypasted block
// recursion

// note that
//     A = B
//     is equivalent to
//     AND A 0
//     XOR A B
// as per Q2, and is used for simplicity

Addstart:
    // XOR for sum
    SUM = X
    XOR SUM Y

    // AND, then left shift for carry
    AND Y X
    CARRY = 0
    // bit 2^0
    A = Y
    AND A 1
    JPZ shiftzero
    XOR CARRY 2
    Shiftzero:
    // bit 2^1
    A = Y
    AND A 2
    JPZ shiftone
    XOR CARRY 4
    Shiftone:
    // bit 2^2
    A = Y
    AND A 4
    JPZ shifttwo
    XOR CARRY 8
    Shifttwo:
    // bit 2^3
    A = Y
    AND A 8
    JPZ shiftthree
    XOR CARRY 16
    Shiftthree:
    // bit 2^4
    A = Y
    AND A 16
    JPZ shiftfour
    XOR CARRY 32
    Shiftfour:
    // bit 2^5
    A = Y
    AND A 32
    JPZ shiftfive
    XOR CARRY 64
    Shiftfive:
    // bit 2^6
    A = Y
    AND A 64
    JPZ shiftsix
    XOR CARRY 128
    Shiftsix:
    // BIT 2^7
    A = Y
    AND A 128
    JPZ shiftseven
    // overflow bit is discarded
    XOR CARRY 255
    Shiftseven:

    // return if no carry
    AND CARRY 255
    JPZ addend

    // loop if carry
    X = SUM
    Y = CARRY
    AND 0 0
    JPZ addstart

Addend:
    X = SUM  // 00110001 = 49
