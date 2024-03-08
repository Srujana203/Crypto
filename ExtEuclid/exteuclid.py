def exteuclid(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def multiplicative_inverse(a, m):
    d, x, y = exteuclid(a, m)
    if d != 1:
        raise ValueError("Inverse does not exist")
    else:
        return x % m


operation = input("Choose operation:\n1. GCD\n2. Multiplicative inverse\nEnter operation number: ")

if operation == '1':
    # GCD operation
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("GCD({},{}) = {}".format(a, b, gcd(a, b)))
elif operation == '2':
    # Multiplicative inverse operation
    a = int(input("Enter number: "))
    m = int(input("Enter modulus: "))
    try:
        inverse = multiplicative_inverse(a, m)
        print("Multiplicative inverse of {} mod {} = {}".format(a, m, inverse))
    except ValueError as e:
        print(e)
else:
    print("Invalid operation number")
