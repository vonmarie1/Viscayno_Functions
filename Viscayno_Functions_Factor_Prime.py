def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return False
    return True


def fp(w, z):
    primes = []
    for num in range(w, z + 1):
        if prime(num):
            primes.append(num)
    return primes


def giv():
    while True:
        x = int(input("Enter a number (start): "))
        y = int(input("Enter a number (end): "))

        if x < 0 or y < 0 or x > y or x == 0:
            print("Enter a valid non-negative range.")
        else:
            return x, y


s, e = giv()
pl = fp(s, e)

if not pl:
    print("There are no prime numbers in this range.")
else:
    print(f"The prime numbers between {s} and {e}: {pl}")
