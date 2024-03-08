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

print("GCD(10012012,2314213):", gcd(10012012, 2314213))
print("GCD(28176412,29108188):", gcd(28176412, 29108188))
print("GCD(38172,23812188):", gcd(38172, 23812188))
print("Multiplicative inverse of 12091 mod 24123123:", multiplicative_inverse(12091, 24123123))
print("Multiplicative inverse of 28173928 mod 129182771:", multiplicative_inverse(28173928, 129182771))
print("GCD(381723029127918237717233210002,23812188332813212739187261):", gcd(381723029127918237717233210002, 23812188332813212739187261))


# operation = input("Choose operation:\n1. GCD\n2. Multiplicative inverse\nEnter operation number: ")

# if operation == '1':
#     # GCD operation
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     print("GCD({},{}) = {}".format(a, b, gcd(a, b)))
# elif operation == '2':
#     # Multiplicative inverse operation
#     a = int(input("Enter number: "))
#     m = int(input("Enter modulus: "))
#     try:
#         inverse = multiplicative_inverse(a, m)
#         print("Multiplicative inverse of {} mod {} = {}".format(a, m, inverse))
#     except ValueError as e:
#         print(e)
# else:
#     print("Invalid operation number")
