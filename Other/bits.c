// negate

int negate(int x) {
    x = ~x + 1 // According to two's compliment rule.
    return x;
}


// bitOr

int bitOr(int x, int y) {
    return ~(~x & ~y); // According to DeMorgan's law.
}


// TMax

int tmax(void) {
    return ~(1 << 31); // Shifting bit to MSb and negating.
}


// fitsShort

int fitsShort (int x) {
    int minus;
    int plus;

    minus = x >> 15;
    minus = minus ^ (~0); // Checking if top 17 bits are all 1's. [3 ops]

    plus = x >> 15;
    plus = plus ^ 0; // Checking if top 17 bits are all 0's. [2 ops]

    return (!minus ^ !plus);
}


// isTmin

int isTmin (int x) {
    int plus;
    int isLowest;

    plus = x + x; // If Tmin, it overflows and becomes 0. [1 op]
    isLowest = (plus | !x); // If both are 0, then it returns 0. [2 ops]

    return !isLowest; // [1 op]
}


// anyEvenBit

int anyEvenBit (int x) {
    int mask;
    int y;

    mask = 0x55 << 24; // Creating a mask where every even bit is 1.
    mask = (0x55 << 16) | mask; // (No rules broken ;) )
    mask = (0x55 << 8) | mask;
    mask = 0x55 | mask; // [6 ops]

    y = x & mask; // Should return 0 if no even bit is on. [1 op]

    return !!y; // To make sure it returns 1 or 0. [2 ops]
}


// getByte

int getByte(int x, int n) {
    int shift;
    int mask;
    int newByte;

    shift = n << 3; // Multiplying n by 8. [1 op]
    mask = 0xFF << shift; // Shifting mask where it's asked for. [1 op]

    newByte = x & mask; // Removing unwanted bits. [1 op]
    newByte = newByte >> shift; // Shifting bits to end [1 op]
    newByte = newByte & 0xFF; // Removing unwanted bits. [1 op]

    return newByte;
}


// isNonNegative

int isNonNegative(int x) {
    int mask;
    int y;

    mask = (1 << 31); // Shift bit to MSb. [1 op]
    y = x & mask; // If y is equal to mask, then x is negative [1 op]

    return !!(y ^ mask); // Double bang for true or false value [3 ops]
}