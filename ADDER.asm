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

    // AND then << for carry
    AND Y X

    // return if no carry
    AND 255 Y
    JPZ addend

    CARRY = 0
    // bit 2^0
    AND 1 Y
    JPZ shiftzero
    XOR CARRY 2
    Shiftzero:
    // bit 2^1
    AND 2 Y
    JPZ shiftone
    XOR CARRY 4
    Shiftone:
    // bit 2^2
    AND 4 Y
    JPZ shifttwo
    XOR CARRY 8
    Shifttwo:
    // bit 2^3
    AND 8 Y
    JPZ shiftthree
    XOR CARRY 16
    Shiftthree:
    // bit 2^4
    AND 16 Y
    JPZ shiftfour
    XOR CARRY 32
    Shiftfour:
    // bit 2^5
    AND 32 Y
    JPZ shiftfive
    XOR CARRY 64
    Shiftfive:
    // bit 2^6
    AND 64 Y
    JPZ shiftsix
    XOR CARRY 128
    Shiftsix:
    // BIT 2^7
    AND 128 Y
    JPZ shiftseven
    // overflow bit is discarded
    XOR CARRY 128
    Shiftseven:

    // return if no carry
    AND 255 CARRY
    JPZ addend

    // loop if carry
    X = SUM
    Y = CARRY
    AND 0 0
    JPZ addstart

Addend:
    X = SUM  // 00110001 = 49
