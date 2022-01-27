// inputs
X = 14  // 00001110
Y = 35  // 00100011


// program

// full adder subroutine
// inputs: A, B, CIN
// outputs: CARRY, SUM
// locals: C, D, E
// jumps to: returnfulladd
Fulladd:
    // intermediaries
    C = A
    AND C B
    D = A
    XOR D B

    // sum output
    SUM = D
    XOR SUM CIN

    // another intermediary
    E = D
    AND E CIN
    // inclusive or operation
    F = E
    XOR F C
    G = E
    AND G C
    XOR F G
    // carry output
    CARRY = F

    // return
    AND 0 0
    JPZ returnfulladd

