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

    // carry output
    E = D
    AND E CIN
    // inclusive or operation
    F = E

    // return
    AND 0 0
    JPZ returnfulladd

