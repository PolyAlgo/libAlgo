import math

def egyptian_multiplication(a, b):
    answer = 0
    # While b different from 0
    while b:
        # We sum all a when b is odd.
        if b % 2:
            answer += a
        a *= 2
        b //= 2
    return answer

def divide_and_conquer_multiplication(a, b):
    # If a or b = 0 then the product is 0.
    if a == 0 or b == 0:
        return 0
    # We calculate the number of digits of the biggest number
    n = int(math.log10(max(a, b))) + 1
    # Cutoff to optimize the calculation
    if n <= 2:
        return a * b
    else:
        # If n is even we cut both the numbers in half
        # If n is odd we add 1 to n to make it even
        if n % 2: n += 1
        a_right = a % (10**(n / 2))
        a_left = a // (10**(n / 2))
        b_right = b % (10**(n / 2))
        b_left = b // (10**(n / 2))
        # Recursively calculate p, q and r
        p = divide_and_conquer_multiplication(a_left, b_left)
        q = divide_and_conquer_multiplication(a_right, b_right)
        r = divide_and_conquer_multiplication(a_left + a_right, b_left + b_right)
        # ab = (aL * 10n/2 + aR) (bL * 10n/2 + bR)
        #    = aL * bL * 10n + aL * bR * 10n/2 + aR * bL * 10n/2 + aR * bR
        #    = aL * bL * 10n + (aL * bR + aR * bL) * 10n/2 + aR * bR
        # where p = aL * bL, q = aR * bR, q = (aL + aR) * (aR + bL)
        # aL * bR + aR * bL = r - p - q
        return int(p * 10**n + (r - p - q) * 10**(n/2) + q)
