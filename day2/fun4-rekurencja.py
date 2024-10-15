# rekurencja
# funkcja wywołuje samą siebie
def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n - 1)


print(silnia(5))


def nwd(a, b):
    if b == 0:
        return a
    return nwd(b, a % b)  # modulo, reszta z dzielenia


print(nwd(48, 18))  # wynik 6
